import pymysql as py
import tkinter as tk
from tkinter import messagebox
import tensorflow as tf
import numpy as np

# Función para cargar el modelo de embeddings
def load_embedding_model():
    model = tf.keras.Sequential([
        tf.keras.layers.InputLayer(input_shape=[], dtype=tf.string),
        tf.keras.layers.TextVectorization(max_tokens=10000),
        tf.keras.layers.Embedding(input_dim=10000, output_dim=512),
        tf.keras.layers.GlobalAveragePooling1D()
    ])
    return model

# Función para preparar el modelo de embeddings con textos
def prepare_embedding_model(model, texts):
    model.layers[0].adapt(texts)  # Ajusta el modelo con los textos proporcionados
    return model

embedding_model = load_embedding_model()  # Carga el modelo de embeddings

# Función para inicializar la base de datos y crear tablas si no existen
def initialize_database():
    conn = py.connect(host='localhost', user='root', password='Moises207')
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS pro")  # Crea la base de datos si no existe
    cursor.execute("USE pro")

    # Crea la tabla de productos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        product_type VARCHAR(255) NOT NULL
    )
    ''')

    # Crea la tabla de compras
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS purchases (
        purchase_id INT AUTO_INCREMENT PRIMARY KEY,
        client_id INT NOT NULL,
        product_id INT NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    ''')

    # Crea la tabla de clientes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        client_id INT AUTO_INCREMENT PRIMARY KEY,
        client_name VARCHAR(255) NOT NULL
    )
    ''')

    # Inserta datos iniciales en la tabla de productos
    cursor.executemany('''
    INSERT INTO products (product_name, product_type)
    VALUES (%s, %s)
    ''', [('Taladro', 'Herramienta'), 
          ('Martillo', 'Herramienta'), 
          ('Destornillador', 'Herramienta'), 
          ('Sierra', 'Herramienta'), 
          ('Cinta métrica', 'Accesorio')])

    conn.commit()
    conn.close()

# Función para obtener textos de productos para adaptar el modelo de embeddings
def get_texts_for_adapt():
    conn = py.connect(host='localhost', user='root', password='Moises207', database='pro')
    cursor = conn.cursor()
    cursor.execute("SELECT product_name FROM products")
    texts = [row[0] for row in cursor.fetchall()]
    conn.close()
    return texts

# Clase principal para la interfaz gráfica de la tienda de bricolaje
class TiendaBricolaje:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Recomendación de Productos")

        self.conn = py.connect(host='localhost', user='root', password='Moises207', database='pro')
        self.cursor = self.conn.cursor()

        texts = get_texts_for_adapt()
        global embedding_model
        embedding_model = prepare_embedding_model(embedding_model, texts)  # Prepara el modelo con textos

        self.current_client_id = None  # Variable para mantener el ID del cliente actual

        self.create_widgets()  # Crea los widgets de la interfaz gráfica

    def create_widgets(self):
        # Widgets para ingresar el nombre del cliente
        self.label_name = tk.Label(self.root, text="Ingrese su nombre:")
        self.label_name.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        # Widgets para ingresar el nombre del producto
        self.label_product = tk.Label(self.root, text="Ingrese el nombre del producto que compró:")
        self.label_product.pack()
        self.product_entry = tk.Entry(self.root)
        self.product_entry.pack()

        # Botones para registrar la compra y obtener recomendaciones
        self.add_purchase_button = tk.Button(self.root, text="Registrar Compra", command=self.add_purchase)
        self.add_purchase_button.pack()
        self.recommend_button = tk.Button(self.root, text="Obtener Recomendaciones", command=self.get_recommendations)
        self.recommend_button.pack()

        # Área de texto para mostrar resultados de recomendaciones
        self.results = tk.Text(self.root, height=15, width=50)
        self.results.pack()

        # Lista para mostrar objetos relacionados (canasta)
        self.basket_label = tk.Label(self.root, text="objetos relacionados:")
        self.basket_label.pack()
        self.basket_list = tk.Listbox(self.root, height=10, width=50)
        self.basket_list.pack()

    # Función para registrar una compra en la base de datos
    def add_purchase(self):
        client_name = self.name_entry.get()
        product_name = self.product_entry.get()
        
        if not client_name or not product_name:
            messagebox.showerror("Error", "Por favor, ingrese el nombre del cliente y el nombre del producto.")
            return

        self.cursor.execute("SELECT client_id FROM clients WHERE client_name = %s", (client_name,))
        client_row = self.cursor.fetchone()
        if client_row:
            self.current_client_id = client_row[0]
        else:
            self.cursor.execute("INSERT INTO clients (client_name) VALUES (%s)", (client_name,))
            self.conn.commit()
            self.current_client_id = self.cursor.lastrowid
        
        self.cursor.execute("SELECT product_id FROM products WHERE product_name = %s", (product_name,))
        product_row = self.cursor.fetchone()
        if not product_row:
            messagebox.showerror("Error", "Nombre del producto no encontrado.")
            return
        
        product_id = product_row[0]

        self.cursor.execute("INSERT INTO purchases (client_id, product_id) VALUES (%s, %s)", (self.current_client_id, product_id))
        self.conn.commit()

        self.update_basket()  # Actualiza la lista de productos comprados
        self.update_embeddings()  # Actualiza el modelo de embeddings

        messagebox.showinfo("Éxito", "Compra registrada con éxito.")

    # Función para actualizar el modelo de embeddings
    def update_embeddings(self):
        texts = get_texts_for_adapt()
        global embedding_model
        embedding_model = prepare_embedding_model(embedding_model, texts)

    # Función para actualizar la lista de productos comprados en la interfaz gráfica
    def update_basket(self):
        if self.current_client_id is None:
            return

        self.basket_list.delete(0, tk.END)
        self.cursor.execute("SELECT p.product_name FROM purchases pu JOIN products p ON pu.product_id = p.product_id WHERE pu.client_id = %s GROUP BY p.product_name LIMIT 5", (self.current_client_id,))
        purchased_products = [row[0] for row in self.cursor.fetchall()]
        for product in purchased_products:
            self.basket_list.insert(tk.END, product)

    # Función para obtener recomendaciones basadas en las compras anteriores
    def get_recommendations(self):
        client_name = self.name_entry.get()
        if not client_name:
            messagebox.showerror("Error", "Por favor, ingrese su nombre.")
            return

        self.cursor.execute("SELECT client_id FROM clients WHERE client_name = %s", (client_name,))
        client_row = self.cursor.fetchone()
        if not client_row:
            messagebox.showerror("Error", "Nombre del cliente no encontrado.")
            return
        
        client_id = client_row[0]
        self.current_client_id = client_id  # Actualiza el ID del cliente actual

        self.cursor.execute("SELECT p.product_name FROM purchases pu JOIN products p ON pu.product_id = p.product_id WHERE pu.client_id = %s", (client_id,))
        purchased_products = [row[0] for row in self.cursor.fetchall()]

        self.cursor.execute("SELECT product_id, product_name FROM products")
        all_products = self.cursor.fetchall()
        
        if not purchased_products:
            messagebox.showinfo("Recomendaciones", "No se encontraron compras anteriores para hacer recomendaciones.")
            return
        
        recommendations = self.generate_recommendations(purchased_products, all_products)
        
        self.results.delete('1.0', tk.END)
        self.results.insert(tk.END, f"Recomendaciones para {client_name} (ID: {client_id}):\n")
        for product_id, product_name in recommendations:
            self.results.insert(tk.END, f"Producto: {product_name} (ID: {product_id})\n")
    
    # Función para generar recomendaciones basadas en la similitud de embeddings
    def generate_recommendations(self, purchased_products, all_products):
        all_product_names = [product_name for _, product_name in all_products]
        all_product_ids = [product_id for product_id, _ in all_products]
        
        product_embeddings = self.get_embeddings(all_product_names)
        purchased_embeddings = self.get_embeddings(purchased_products)
        
        cosine_similarities = self.calculate_cosine_similarity(purchased_embeddings, product_embeddings)
        
        avg_similarities = np.mean(cosine_similarities, axis=0)
        product_scores = list(zip(all_product_ids, avg_similarities))
        sorted_recommendations = sorted(product_scores, key=lambda x: x[1], reverse=True)
        
        purchased_product_ids = [self.get_product_id(name) for name in purchased_products]
        recommendations = [(product_id, self.get_product_name(product_id)) for product_id, _ in sorted_recommendations if product_id not in purchased_product_ids]
        
        return recommendations

    # Función para obtener los embeddings de los nombres de productos
    def get_embeddings(self, product_names):
        product_names_tensor = tf.constant(product_names)
        return embedding_model(product_names_tensor)

    # Función para calcular la similitud coseno entre dos matrices
    def calculate_cosine_similarity(self, matrix1, matrix2):
        matrix1 = tf.cast(matrix1, dtype=tf.float32)
        matrix2 = tf.cast(matrix2, dtype=tf.float32)
        norm_matrix1 = tf.linalg.norm(matrix1, axis=1, keepdims=True)
        norm_matrix2 = tf.linalg.norm(matrix2, axis=1, keepdims=True)
        dot_product = tf.matmul(matrix1, matrix2, transpose_b=True)
        norm_product = tf.matmul(norm_matrix1, norm_matrix2, transpose_b=True)
        return dot_product / norm_product

    # Función para obtener el ID de un producto por su nombre
    def get_product_id(self, product_name):
        self.cursor.execute("SELECT product_id FROM products WHERE product_name = %s", (product_name,))
        row = self.cursor.fetchone()
        return row[0] if row else None

    # Función para obtener el nombre de un producto por su ID
    def get_product_name(self, product_id):
        self.cursor.execute("SELECT product_name FROM products WHERE product_id = %s", (product_id,))
        row = self.cursor.fetchone()
        return row[0] if row else None

# Función principal para ejecutar la aplicación
def main():
    initialize_database()  # Inicializa la base de datos
    
    root = tk.Tk()
    app = TiendaBricolaje(root)  # Crea una instancia de la aplicación
    root.mainloop()  # Ejecuta el bucle principal de la interfaz gráfica

if __name__ == "__main__":
    main()
