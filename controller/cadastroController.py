from PyQt5 import uic, QtWidgets
import mysql.connector 
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "cadastro_anuncio"
)

def funcao_principal():
    nomeDoAnuncio = formulario.lineEdit.text()
    cliente = formulario.lineEdit_2.text()
    dataDeinicio = formulario.lineEdit_3.text()
    dataDeTermino = formulario.lineEdit_4.text()
    investimentoDiario = formulario.lineEdit_5.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO anuncio (nome_anuncio, cliente, data_inicio, data_fim, investimento) VALUES (%s, %s, %s, %s, %s )"
    dados = (str(nomeDoAnuncio), str(cliente), str(dataDeinicio), str(dataDeTermino), str(investimentoDiario))
    cursor.execute(comando_SQL, dados)
    banco.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")

def funcao_relatorio():
    relatorio.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM anuncio"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)

    relatorio.tableWidget.setRowCount(len(dados_lidos))
    relatorio.tableWidget.setColumnCount(4)
    for i in range(-1, len(dados_lidos)):
            relatorio.tableWidget.setItem(i, 0 , QtWidgets.QTableWidgetItem(str(dados_lidos[i][5])))
            relatorio.tableWidget.setItem(i, 1 , QtWidgets.QTableWidgetItem(str(dados_lidos[i][5] * 30)))
            relatorio.tableWidget.setItem(i, 2 , QtWidgets.QTableWidgetItem(str(dados_lidos[i][5] * 30 * 0.12)))
            relatorio.tableWidget.setItem(i, 3 , QtWidgets.QTableWidgetItem(str(dados_lidos[i][5] * 30 * 0.12 * 0.15)))  

def gerar_pdf():
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM anuncio"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    y = 0
    pdf = canvas.Canvas("cadastro_anuncio.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Anuncios cadastrados:")
    pdf.setFont("Times-Bold", 18)

    pdf.drawString(10, 750, "ID")
    pdf.drawString(110, 750, "NOME ANÚNCIO")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(dados_lidos[i][0]))
        pdf.drawString(110, 750 - y, str(dados_lidos[i][1]))
    pdf.save()
    print("PDF FOI GERADO COM SUCESSO!")


app = QtWidgets.QApplication([])
formulario = uic.loadUi("page01.ui")
relatorio = uic.loadUi("page02.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(funcao_relatorio)
relatorio.pushButton_2.clicked.connect(gerar_pdf)
formulario.show()
app.exec()