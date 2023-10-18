import sqlite3
import xml.etree.ElementTree as ET

# Connect to the SQLite database
conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()

# Retrieve enabled products from the product table
cursor.execute("SELECT * FROM product WHERE status = '1'")
products = cursor.fetchall()

# Create the root element
root = ET.Element('rss', attrib={'version': '2.0'})
channel = ET.SubElement(root, 'channel')

# Iterate through the products and create XML elements
for product in products:
    product_id, model, ean, quantity, image, manufacturer_id, price, status = product

    # Retrieve additional images and sort them from the product_image table
    cursor.execute("SELECT image FROM product_image WHERE product_id = ? ORDER BY sort_order", (product_id,))
    additional_images = [row[0] for row in cursor.fetchall()]

    # Retrieve manufacturer name from the manufacturer table
    cursor.execute("SELECT name FROM manufacturer WHERE manufacturer_id = ?", (manufacturer_id,))
    manufacturer_name = cursor.fetchone()[0]


    # Retrieve product name and description from the product_description table
    cursor.execute("SELECT name, description FROM product_description WHERE product_id = ?", (product_id,))
    name, description = cursor.fetchone()

    item = ET.SubElement(channel, 'item')
    ET.SubElement(item, 'id').text = str(product_id)
    ET.SubElement(item, 'title').text = name
    ET.SubElement(item, 'description').text = description
    ET.SubElement(item, 'link').text = f'https://butopea.com/p/{product_id}'
    ET.SubElement(item, 'image_link').text = image
    for additional_image in additional_images:
        ET.SubElement(item, 'additional_image_link').text = additional_image
    ET.SubElement(item, 'availability').text = 'in stock'  # You can adjust availability as needed
    ET.SubElement(item, 'price').text = f'{price} HUF'
    ET.SubElement(item, 'brand').text = manufacturer_name
    ET.SubElement(item, 'condition').text = 'new'

# Create an ElementTree object and save it to a file
tree = ET.ElementTree(root)
tree.write('feed.xml', encoding='utf-8')

# Close the database connection
conn.close()

print('Product feed created successfully as feed.xml')
