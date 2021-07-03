from PyQt5 import uic, QtWidgets

def funcao_principal():
    nomeDoAnuncio = formulario.lineEdit.text()
    cliente = formulario.lineEdit_1.text()
    dataDeinicio = formulario.lineEdit_3.text()
    dataDeTermino = formulario.lineEdit_4.text()
    investimentoDiario = formulario.lineEdit_5.text()

    print("teste")
    print("Nome do anúncio: ", nomeDoAnuncio)

app = QtWidgets.QApplication([])
formulario = uic.loadUi("page01.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()