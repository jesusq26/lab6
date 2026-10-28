def parsear_producto(linea):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        dict: {"codigo" : codigo:str, "nombre" : nombre:str, "precio" : precio:float, "cantidad" : cantidad:int}
    """
    datos = linea.split(",")
    if len(datos) != 4:
        raise ValueError("Debe haber 4 datos")
    codigo = str(datos[0])
    nombre = str(datos[1])
    try:
        precio = float(datos[2].strip())
    except:
        raise ValueError("Precio no valido")
    if precio < 0:
        raise ValueError("Precio no valido")
    try:
        cantidad = int(datos[3].strip())
    except:
        raise ValueError("Cantidad no valida")
    if cantidad < 0:
        raise ValueError("Cantidad no valida")
    dict = {"codigo": codigo, "nombre": nombre, "precio": precio, "cantidad": cantidad}
    return dict

def resumen_de_producto(linea):
    """
    Entrada:
        linea: str con formato "codigo,nombre,precio,cantidad"
    Salida:
        str: "CODIGO - NOMBRE: $VALOR" (VALOR = precio*cantidad redondeado a 1 decimal)
    """
    P = parsear_producto(linea)
    valor = P["precio"] * P["cantidad"]
    valor_redondeado = round(valor, 1)
    return f"{P['codigo']} - {P['nombre']}: ${valor_redondeado}"

def _validar_lineas(lineas):
    if type(lineas) != list or len(lineas) == 0:
        raise ValueError("Debe ser una lista no vacia")
    for i in lineas:
        if type(i) != str:
            raise ValueError("Todos los elementos deben ser str")

def resumen_de_lotes(lineas: list) -> list:
    """
    Entrada:
        lines: list de str, no vacía
    Salida:
        list de str con resúmenes por producto (usa resumen_de_producto)
    """
    _validar_lineas(lineas)
    y = []
    for i in lineas:
        y.append(resumen_de_producto(i))
    return y


def valor_de_lote(lineas: list) -> float:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        float: valor total (suma de precio*cantidad) redondeado a 1 decimal
    """
    _validar_lineas(lineas)
    valort = 0.0
    for a in lineas:
        P = parsear_producto(a)
        valort = valort + P["precio"] * P["cantidad"]
    return round(valort, 1)

def producto_maximo_valor(lineas: list) -> str:
    """
    Entrada:
        lineas: list de str, no vacía
    Salida:
        str: resumen del producto de mayor (precio*cantidad). En empate, el primero.
    """
    _validar_lineas(lineas)
    mejor = parsear_producto(lineas[0])
    mejor_valor = mejor["precio"] * mejor["cantidad"]
    for a in lineas[1:]:
        P = parsear_producto(a)
        valor = P["precio"] * P["cantidad"]
        if valor > mejor_valor:
            mejor = P
            mejor_valor = valor
    return f"{mejor['codigo']} - {mejor['nombre']}: ${round(mejor_valor, 1)}"


if __name__ == "__main__":
    products = [
        "P001,Lapiz,0.5,100",
        "P002,Cuaderno,1.25,50",
        "P003 , Borrador ,1.35 , 10"
    ]
    
    print(resumen_de_producto(products[0]))       # "P001 - Lapiz: $50.0"
    print(resumen_de_lotes(products))             # ["P001 - ...", "P002 - ...", "P003 - ..."]
    print(valor_de_lote(products))                # 126.0
    print(producto_maximo_valor(products))        # "P002 - Cuaderno: $62.5"
