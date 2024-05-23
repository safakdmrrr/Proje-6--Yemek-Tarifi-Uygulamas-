import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox, QListWidget, QListWidgetItem

class Tarif:
    def __init__(self, ad, malzemeler, yapilis):
        self.ad = ad
        self.malzemeler = malzemeler
        self.yapilis = yapilis
        self.puan = None

    def puan_ver(self, puan):
        self.puan = puan

class TarifYoneticisi:
    def __init__(self):
        self.tarifler = []

    def tarif_ekle(self, tarif):
        self.tarifler.append(tarif)
        QMessageBox.information(None, "Bilgi", f"'{tarif.ad}' tarifi başarıyla eklendi..")

    def tarif_ara(self, yemek):
        bulunan_tarifler = []
        for tarif in self.tarifler:
            if tarif.ad.lower() == yemek.lower():
                bulunan_tarifler.append(tarif)
        return bulunan_tarifler

    def tarif_puanla(self, ad, puan):
        for tarif in self.tarifler:
            if tarif.ad == ad:
                tarif.puan_ver(puan)
                QMessageBox.information(None, "Bilgi", f"'{ad}' tarifine {puan} puan verildi.")
                return
        QMessageBox.warning(None, "Uyarı", f"'{ad}' tarifi bulunamadı.")

class Arayuz(QWidget):
    def __init__(self):
        super().__init__()
        self.admin = TarifYoneticisi()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Tarif Ekle
        layout_ekle = QVBoxLayout()
        lbl_ad = QLabel("Tarif Adı:")
        self.input_ad = QLineEdit()
        self.input_ad.setPlaceholderText("Tarif adını giriniz")
        layout_ekle.addWidget(lbl_ad)
        layout_ekle.addWidget(self.input_ad)

        lbl_malzemeler = QLabel("Malzemeler:")
        self.input_malzemeler = QTextEdit()
        self.input_malzemeler.setPlaceholderText("Malzemeleri giriniz")
        layout_ekle.addWidget(lbl_malzemeler)
        layout_ekle.addWidget(self.input_malzemeler)

        lbl_yapilis = QLabel("Yapılışı:")
        self.input_yapilis = QTextEdit()
        self.input_yapilis.setPlaceholderText("Yapılış adımlarını giriniz")
        layout_ekle.addWidget(lbl_yapilis)
        layout_ekle.addWidget(self.input_yapilis)

        btn_ekle = QPushButton("Tarif Ekle")
        btn_ekle.clicked.connect(self.tarif_ekle)
        layout_ekle.addWidget(btn_ekle)
        layout.addLayout(layout_ekle)

        # Tarif Ara
        layout_ara = QHBoxLayout()
        lbl_ara = QLabel("Aranacak Tarif Adı:")
        self.input_ara = QLineEdit()
        self.input_ara.setPlaceholderText("Aranacak tarifi giriniz")
        btn_ara = QPushButton("Tarif Ara")
        btn_ara.clicked.connect(self.tarif_ara)
        layout_ara.addWidget(lbl_ara)
        layout_ara.addWidget(self.input_ara)
        layout_ara.addWidget(btn_ara)
        layout.addLayout(layout_ara)

        # Tarif Puanla
        layout_puanla = QHBoxLayout()
        lbl_puanla_ad = QLabel("Puan Verilecek Tarif Adı:")
        self.input_puanla_ad = QLineEdit()
        self.input_puanla_ad.setPlaceholderText("Puan vermek istediğiniz tarifin adını giriniz")
        lbl_puan = QLabel("Puan (1-5):")
        self.input_puan = QLineEdit()
        self.input_puan.setPlaceholderText("1 ile 5 arasında bir puan giriniz")
        btn_puanla = QPushButton("Tarife Puan Ver")
        btn_puanla.clicked.connect(self.tarif_puanla)
        layout_puanla.addWidget(lbl_puanla_ad)
        layout_puanla.addWidget(self.input_puanla_ad)
        layout_puanla.addWidget(lbl_puan)
        layout_puanla.addWidget(self.input_puan)
        layout_puanla.addWidget(btn_puanla)
        layout.addLayout(layout_puanla)

        # Tarif Listesi
        self.liste_widget = QListWidget()
        layout.addWidget(self.liste_widget)

        self.setLayout(layout)

    def tarif_ekle(self):
        ad = self.input_ad.text()
        malzemeler = self.input_malzemeler.toPlainText().split("\n")
        yapilis = self.input_yapilis.toPlainText().split("\n")
        tarif = Tarif(ad, malzemeler, yapilis)
        self.admin.tarif_ekle(tarif)

    def tarif_ara(self):
        ad = self.input_ara.text()
        bulunan_tarifler = self.admin.tarif_ara(ad)
        self.liste_widget.clear()
        if bulunan_tarifler:
            for tarif in bulunan_tarifler:
                malzemeler_str = ", ".join(tarif.malzemeler)
                yapilis_str = "\n".join(tarif.yapilis)
                self.liste_widget.addItem(f"Adı: {tarif.ad}\nMalzemeler: {malzemeler_str}\nYapılışı: {yapilis_str}")
        else:
            QMessageBox.warning(None, "Uyarı", f"'{ad}' adında bir tarif bulunamadı.")

    def tarif_puanla(self):
        ad = self.input_puanla_ad.text()
        puan = int(self.input_puan.text())
        if puan < 1 or puan > 5:
            QMessageBox.warning(None, "Uyarı", "Geçersiz puan! Puan 1 ile 5 arasında olmalı.")
            return
        self.admin.tarif_puanla(ad, puan)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Arayuz()
    window.setWindowTitle("Tarif Yönetim Sistemi")
    window.show()
    sys.exit(app.exec_())








