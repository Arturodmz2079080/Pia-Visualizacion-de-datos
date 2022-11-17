from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import  QDialog
import mysql.connector
from PyQt5.uic import loadUi

from datetime import date
from decimal import *




#iniciar la app
app= QtWidgets.QApplication([])
login= uic.loadUi("Ventana 2.ui")
menu= uic.loadUi("MenuEmpleado.ui")
eleccion= uic.loadUi("MenuGerente.ui")
V_empleado = uic.loadUi("Ventana 1.ui")
V_cliente = uic.loadUi("ClientesGuardar.ui")
productos = uic.loadUi("Productos.ui")
cuchillos=uic.loadUi("ProductosCuchillos.ui")
ollas=uic.loadUi("ProductosOllas.ui")
herramientas=uic.loadUi("ProductosHerramientas.ui")
accesorios=uic.loadUi("ProductosAccesorios.ui")


def conexion_base():
    conexion = mysql.connector.connect(
        user = "root",
        password= "Minecraft02",
        host = "localhost",
        database = "LAS_HERRAMIENTAS_DEL_GORDO",
        port= "3306")
    return conexion

Carrito_compra=[(0,"",0)]

#ejemplo de uso (recuerda cerrar el cursor al terminar de usarlo)
"""
conexion = conexion_base()
c=conexion.cursor()
c.execute("select * from empleados;")
data = c.fetchall()

print(data)

conexion.commit()"""


class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("Punto de venta.ui",self)

        self.initUI()

    def initUI(self):
        
        self.datosTabla()
        self.verificar()
        self.carros()
        self.pagar()

        Busca = self.btnBuscar
        salir = self.btnSalir
        verificar=self.btnVerificar
        carro=self.btnAgregar
        pagar=self.btnPagar
        #carro=self.btnCarrito

        #accion de los botones
        pagar.clicked.connect(self.pagar)
        carro.clicked.connect(self.carros)
        verificar.clicked.connect(self.verificar)
        Busca.clicked.connect(self.datosTabla)
        salir.clicked.connect(app.quit)
        #carro.clicked.connect(self.Carrito)

    def datosTabla(self):

        eleccion_categoria=self.cmbCategoria.currentText()
        if eleccion_categoria=="Accesorios":
            conexion = conexion_base()
            c=conexion.cursor()
            c.execute('select Id_Producto, Nombre_de_Producto, Precio_de_Producto, Categoria, Proveedor from productos where Categoria="Accesorios";')
            data_Accesorios=c.fetchall()
            row=0
            self.tableWidget.setRowCount(len(data_Accesorios))
            for i in data_Accesorios:
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(i[3]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(i[4]))
                row += 1
            c.close()
            conexion.commit()
        elif eleccion_categoria=="Herramientas de cocina":
            conexion = conexion_base()
            c=conexion.cursor()
            c.execute('select Id_Producto, Nombre_de_Producto, Precio_de_Producto, Categoria, Proveedor from productos where Categoria="Herramientas";')
            data_Accesorios=c.fetchall()
            row=0
            self.tableWidget.setRowCount(len(data_Accesorios))
            for i in data_Accesorios:
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(i[3]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(i[4]))
                row += 1
            c.close()
            conexion.commit()
        elif eleccion_categoria=="Sartenes":
            conexion = conexion_base()
            c=conexion.cursor()
            c.execute('select Id_Producto, Nombre_de_Producto, Precio_de_Producto, Categoria, Proveedor from productos where Categoria="Sartenes";')
            data_Accesorios=c.fetchall()
            row=0
            self.tableWidget.setRowCount(len(data_Accesorios))
            for i in data_Accesorios:
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(i[3]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(i[4]))
                row += 1
            c.close()
            conexion.commit()
        elif eleccion_categoria=="Cuchillos":
            conexion = conexion_base()
            c=conexion.cursor()
            c.execute('select Id_Producto, Nombre_de_Producto, Precio_de_Producto, Categoria, Proveedor from productos where Categoria="Cuchillos";')
            data_Accesorios=c.fetchall()
            row=0
            self.tableWidget.setRowCount(len(data_Accesorios))
            for i in data_Accesorios:
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(i[3]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(i[4]))
                row += 1
            c.close()
            conexion.commit()
        elif eleccion_categoria=="Ollas":
            conexion = conexion_base()
            c=conexion.cursor()
            c.execute('select Id_Producto, Nombre_de_Producto, Precio_de_Producto, Categoria, Proveedor from productos where Categoria="Ollas";')
            data_Accesorios=c.fetchall()
            row=0
            self.tableWidget.setRowCount(len(data_Accesorios))
            for i in data_Accesorios:
                self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(i[0])))
                self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i[1]))
                self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(i[2])))
                self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(i[3]))
                self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(i[4]))
                row += 1

            c.close()
            conexion.commit()

    def verificar(self):
        cliente=self.txtIDCliente.text()
        conexion = conexion_base()
        c=conexion.cursor()
        c.execute("select Id_Cliente,Credito_decimal, Saldo_decimal from clientes;")
        idc=c.fetchall()
        conexion.commit()

        verificado=0
        for i in idc:
            if str(i[0])==cliente:
                verificado+=1
                credito=i[1]
                saldo=i[2]
                
        if verificado==1:
            self.lblNotacliente.setText("Numero de Cliente valido")
            self.lblCredito.setText(str(credito))
            self.lblSaldo.setText(str(saldo))
        else:
            self.lblNotacliente.setText("Numero de Cliente invalido")
        

            
        

    def carros(self):
        codigo=self.txtIDProducto.text()
        cantidad=self.spinBox.value()
        conexion = conexion_base()
        c=conexion.cursor()
        c.execute('select Id_Producto, Nombre_de_Producto, Precio_de_Producto, Categoria, Proveedor from productos;')
        idc=c.fetchall()

        descripcion=""
        Precio=""
        verificado=0
        subtotal=0
        for x in idc:
            if codigo == str(x[0]):
                verificado+=1
                descripcion=x[1]
                Precio=x[2]

        row=self.twCarro.rowCount()
        if verificado==1:
            self.twCarro.setRowCount(row + 1)
            self.lblNotaproducto.setText("codigo de producto valido")
            self.twCarro.setItem(row,0,QtWidgets.QTableWidgetItem(str(cantidad)))
            self.twCarro.setItem(row,1,QtWidgets.QTableWidgetItem(str(descripcion)))
            self.twCarro.setItem(row,2,QtWidgets.QTableWidgetItem(str(Precio)))
            pedido = (cantidad,descripcion,Precio)
            Carrito_compra.append(pedido)
            for x in Carrito_compra:
                subtotal += Decimal(x[0]) + Decimal(x[2])
            total = Decimal(Decimal(subtotal)*Decimal(1.16).quantize(Decimal('.01'), rounding=ROUND_UP))
            self.label1_4.setText(str(total))

        else:
            self.lblNotaproducto.setText("codigo de producto invalido")
            
        print(self.twCarro.items)
        c.close()
        conexion.commit()
    

    def pagar(self):
        codigo=self.txtIDCliente.text()
        pago=self.txtPago.text()
        subtotal=0
        
        conexion = conexion_base()
        c=conexion.cursor()
        c.execute("select Id_Cliente from clientes;")
        idc=c.fetchall()
        c.close()
        conexion.commit()
        verificado=0
        for i in idc:
            if str(i[0])==codigo:
                verificado+=1
        for x in Carrito_compra:

            subtotal += Decimal(x[0]) + Decimal(x[2])
        total = Decimal(Decimal(subtotal)*Decimal(1.16).quantize(Decimal('.01'), rounding=ROUND_UP))
        TOTALes =Decimal(pago) - total
        if verificado==1:
            if TOTALes>0:
                self.lblNotaCompra.setText("compra realizada\nvuelva pronto")
                self.lblCambio.setText(str(TOTALes))
                self.txtPago.setText("")
                self.txtIDCliente.setText("")
                self.txtIDProducto.setText("")
                self.label1_4.setText("")
                self.lblSaldo.setText("")
                self.lblCredito.setText("")
                self.twCarro.clearContents()
                self.twCarro.setRowCount(0)
            else:
                self.lblNotaCompra.setText("su pago es inferior\nal monto a pagar")
        else:
            self.lblNotaCompra.setText("Numero de Cliente incorrecto\nverifique su ID")


mainwindow=MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1230)





#cargar archivos .ui

def gui_login_menu():
    nombre = login.lblUsuario.text()
    contraseña = login.lblContra.text()
    #puesto = login.cmbPuesto.currentText()
    conexion=conexion_base()
    c=conexion.cursor()
    c.execute("select Nombre_de_usuario,Contraseña,Tipo_de_Empleado from empleados")
    data=c.fetchall()
    if len(nombre)==0 or len(contraseña)==0:
            login.lblNota.setText("Un campo de datos esta en blanco")
    for i in data:
        puesto = int(i[2])
        if nombre==str(i[0]) and contraseña==str(i[1]) and puesto==2:
            entrada_menu()
            
        elif nombre==str(i[0]) and contraseña==str(i[1]) and puesto==1:
            entrada_registro()
        else:
            login.lblNota.setText("Usuario o contraseña incorrectos")

def menu_productos():
    cuchillos.hide()
    ollas.hide()
    herramientas.hide()
    accesorios.hide()
    productos.show()

def entrada_menu():
    login.hide()
    productos.hide()
    menu.show()
def entrada_registro():
    login.hide()
    eleccion.show()
def gui_salir():
    app.exit()
def registro_empleado():
    eleccion.hide()
    V_empleado.show()
def registro_cliente():
    eleccion.hide()
    menu.hide()
    V_cliente.show()
def Cuchillos():
    productos.hide()
    cuchillos.show()
def Ollas():
    productos.hide()
    ollas.show()
def Herramientas():
    productos.hide()
    herramientas.show()
def Accesorios():
    productos.hide()
    accesorios.show()

def Carro():# cambio
    eleccion.hide()
    menu.hide()
    widget.show()
def Productos():
    menu.hide()
    eleccion.hide()
    productos.show()
def guardar_empleado():
    nombre=V_empleado.txtNombre.text()
    apellidop=V_empleado.txtApaterno.text()
    apellidom=V_empleado.txtAmaterno.text()
    nacimiento=V_empleado.txtNacimiento.text()
    telefono=V_empleado.txtTelefono.text()
    puesto=V_empleado.txtPuesto.text()
    usuario=V_empleado.txtNusuario.text()
    contraseña=V_empleado.txtContra.text()
    tipo=V_empleado.txtTipo.text()
    id=V_empleado.txtID.text()
    contrata=V_empleado.txtContrato.text()
    
    conexion = conexion_base()
    c=conexion.cursor()
    c.execute(f"INSERT INTO Empleados (Id_Empleado, Nombre, Apellido_Paterno,Apellido_Materno, Fecha_de_Nacimiento, Celular, Puesto, Fecha_de_contratacion, Estado, Nombre_de_usuario, Contraseña, Tipo_de_Empleado) VALUES ({id}, '{nombre}','{apellidop}','{apellidom}', '{nacimiento}', {telefono}, '{puesto}', '{contrata}', true , '{usuario}', '{contraseña}', '{tipo}');")

    conexion.commit()

def Guardar_cliente():
    nombre=V_cliente.lineEdit.text()
    apellidop=V_cliente.lineEdit_2.text()
    apellidom=V_cliente.lineEdit_3.text()
    correo=V_cliente.lineEdit_5.text()
    direccion=V_cliente.lineEdit_6.text()
    ids=V_cliente.lineEdit_10.text()
    credito=V_cliente.lineEdit_10.text()
    saldo=V_cliente.lineEdit_10.text()
    
    conexion = conexion_base()
    c=conexion.cursor()
    c.execute(f"INSERT INTO Clientes (Id_Cliente, Nombre, Apellido_Paterno, Apellido_Materno, Direccion, Correo, Estado, Credito_decimal, Saldo_decimal) VALUES ({ids}, '{nombre}' , '{apellidop}', '{apellidom}', '{direccion}', '{correo}', TRUE, {credito }, {saldo});")

    conexion.commit()

def graficas():
    conexion = conexion_base()
    c=conexion.cursor()
    c.execute("SELECT Proveedor FROM Productos order by Proveedor;")
    data=c.fetchall()

    conexion.commit()
    mayores=0
    menores=0
    uno=0
    dia=date.today()
    for i in data:
        for j in i:
            if (dia-j)<1:
                uno+=1
            elif (dia-j)<5:
                menores+=1
            else:
                mayores+=1
    print(mayores)
    print(menores)
    print(uno)



herramientas.pushButton.clicked.connect(menu_productos)
herramientas.btnSalir.clicked.connect(gui_salir)
ollas.pushButton.clicked.connect(menu_productos)
ollas.btnSalir.clicked.connect(gui_salir)
accesorios.pushButton.clicked.connect(menu_productos)
accesorios.btnSalir.clicked.connect(gui_salir)
cuchillos.pushButton.clicked.connect(menu_productos)
cuchillos.btnSalir.clicked.connect(gui_salir)

V_cliente.btnGuardar.clicked.connect(Guardar_cliente)
V_cliente.btnSalir.clicked.connect(gui_salir)

V_empleado.btnGuardar.clicked.connect(guardar_empleado)
V_empleado.btnSalir.clicked.connect(gui_salir)

productos.btnCuchillos.clicked.connect(Cuchillos)
productos.btnOllas.clicked.connect(Ollas)
productos.btnHerramientas.clicked.connect(Herramientas)
productos.btnAccesorios.clicked.connect(Accesorios)
productos.btnMenu.clicked.connect(entrada_menu)

menu.btnProductos.clicked.connect(Productos)
menu.btnCarrito.clicked.connect(Carro)#cambio
menu.btnClientes.clicked.connect(registro_cliente)
menu.btnSalir.clicked.connect(gui_salir)

eleccion.btnEmpleado.clicked.connect(registro_empleado)
eleccion.btnCliente.clicked.connect(registro_cliente)
eleccion.btnVenta.clicked.connect(Carro)
eleccion.btnProductos.clicked.connect(Productos)
eleccion.btnSalir.clicked.connect(gui_salir)

login.btnSiguiente.clicked.connect(gui_login_menu)
login.btnSalir.clicked.connect(gui_salir)

login.show()
app.exec()
