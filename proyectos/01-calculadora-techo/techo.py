# Calculadora de costo de techo — Mini proyecto 1
# Todos los valores son ficticios, solo para practicar.

# --- Datos base ---
# Costo de material del proveedor, USD por square (1 SQ = 100 pies²)
costo_material_sq = {'asfalto': 150, 'metal': 250, 'teja': 80}
mano_obra_sq = 300        # USD por square
margen = 0.25            # 25 % de ganancia
desperdicio = 1.10       # 10 % extra de material

# --- Entrada de datos ---
largo = float(input('Dime el largo del techo (pies): '))
ancho = float(input('Dime el ancho del techo (pies): '))
material = input('Material (asfalto/metal/teja): ').lower()
presupuesto = float(input('Presupuesto del cliente (USD): '))

# --- Área ---
area = largo * ancho                          # pies²
squares = round(area * desperdicio / 100, 2)  # SQ con desperdicio

# --- Costo del material elegido ---
material_total = squares * costo_material_sq[material]
mano_obra_total = squares * mano_obra_sq
subtotal = material_total + mano_obra_total
precio_cliente = round(subtotal * (1 + margen), 2)

# --- Comparación de los 3 materiales (precio al cliente) ---
precio_asfalto = round((squares * costo_material_sq['asfalto'] + mano_obra_total) * (1 + margen), 2)
precio_metal = round((squares * costo_material_sq['metal'] + mano_obra_total) * (1 + margen), 2)
precio_teja = round((squares * costo_material_sq['teja'] + mano_obra_total) * (1 + margen), 2)
comparacion = [precio_asfalto, precio_metal, precio_teja]

# --- Comparadores ---
alcanza = precio_cliente <= presupuesto
techo_grande = area > 2000

# --- Resumen ---
print('\n----- RESUMEN -----')
print(f'Área: {area} pies² | Squares con desperdicio: {squares}')
print(f'Material: {material}')
print(f'Costo material: USD {round(material_total, 2)}')
print(f'Mano de obra:   USD {round(mano_obra_total, 2)}')
print(f'Subtotal:       USD {round(subtotal, 2)}')
print(f'Precio cliente: USD {precio_cliente}')
print(f'Comparación (asfalto, metal, teja): {comparacion}')
print(f'¿Alcanza el presupuesto? {alcanza}')
print(f'¿Techo grande? {techo_grande}')