from mainWindow import *
import sqlite3
import datetime as dt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    dataBase = None
    connectDB = None
    def __init__(self, *args, **kwargs):
        global dataBase, connectDB
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        # Establecer la Conección de la base de datos
        dataBase, connectDB = self.connectionDataBase()
        # self.createTable(dataBase)#En que la base de datos sea nueva, Descomentar para crear la tabla.

        self.setupUi(self)
        # Funcionamiento de los botones
        self.bGuardReg.clicked.connect(self.saveUser)
        self.bBuscar.clicked.connect(self.showById)
        self.bDelete.clicked.connect(self.deleteById)
        self.bUpdate.clicked.connect(self.updateId)



    def saveUser(self):
        global dataBase, connectDB
        # Obtener los datos de la interfaz
        values = self.getDataForm()

        # Sql de insert a SqLite
        sql = 'INSERT INTO users (name,edad,genero,fecha,peso,talla,hora,areaTrabajo,timpoLabora,habitos,actividad,tiempoRiesgo,medicamento,dolorMano,dolorManoDer,dolorManoIzq,dolorManoInt,dolorManoFcia,dolorManoLocal,dolorManoIrrad,dolorCuello,dolorCuello2,dolorCuello3,dolorCuello4,dolorCuello5,dolorCuello6,dolorCuello7,dolorHombro,dolorHombro2,dolorHombro3,dolorHombro4,dolorHombro5,dolorHombro6,dolorHombro7,dolorEspalda,dolorEspalda2,dolorEspalda3,dolorEspalda4,dolorEspalda5,dolorEspalda6,dolorEspalda7,adormeMano,adormeMano2,adormeMano3,adormeMano4,adormeMano5,adormeMano6,adormeMano7,dismiMovMano,dismiMovMano2,dismiMovMano3,dismiMovMano4,dismiMovMano5,dismiMovMano6,dismiMovMano7,perdidaFuMano,perdidaFuMano2,perdidaFuMano3,perdidaFuMano4,perdidaFuMano5,perdidaFuMano6,perdidaFuMano7,torpeMano,torpeMano2,torpeMano3,torpeMano4,torpeMano5,torpeMano6,torpeMano7,senExMano,senExMano2,senExMano3,senExMano4,senExMano5,senExMano6,senExMano7,otrosMole,obserDefor,obserInf,obserAtro,obserCam,dmMusBrazoDer,dmMusBrazoIzq,dmMusAnBrazoDer,dmMusAnBrazoIzq,rMFleCD,rMFleCI,rMFleHD,rMFleHI,rMFleCoD,rMFleCoI,rMFleMD,rMFleMI,rMFleDD,rMFleDI,rMExtCD,rMExtCI,rMExtHD,rMExtHI,rMExtCoD,rMExtCoI,rMExtMD,rMExtMI,rMExtDD,rMExtDI,rMAdbCD,rMAdbCI,rMAdbHD,rMAdbHI,rMAdbCoD,rMAdbCoI,rMAdbMD,rMAdbMI,rMAdbDD,rMAdbDI,rMAduCD,rMAduCI,rMAduHD,rMAduHI,rMAduCoD,rMAduCoI,rMAduMD,rMAduMI,rMAduDD,rMAduDI,rMRotExtCD,rMRotExtCI,rMRotExtHD,rMRotExtHI,rMRotExtCoD,rMRotExtCoI,rMRotExtMD,rMRotExtMI,rMRotExtDD,rMRotExtDI,rMRotInCD,rMRotInCI,rMRotInHD,rMRotInHI,rMRotInCoD,rMRotInCoI,rMRotInMD,rMRotInMI,rMRotInDD,rMRotInDI,rFMPrePalmaD,rFMPrePalmaI,rFMPreDigD,rFMPreDigI,rSenPMonoD,rSenPMonoI,rSenVibroD,rSenVibroI,rSenDisD,rSenDisI,sESFlickD,sESFlickI,sESPhallenD,sESPhallenI,sESTinelD,sESTinelI,sESCirculoD,sESCirculoI,eCerviRes,eCerviTRes,eCerviOcc,eCerviC1,eCerviC2,eCerviC3,eCerviC4,eCerviC5,eCerviC6,eCerviC7,eDorsPiRod,eDorsPreDir,eDorsPreLat,eDorsPreAD,eIliacosTPie,eIliacosTPos,eIliacosEias,eIliacosTAlar,eIliacosTAcor,eSacroTArSen,eSacroTRot,eSacroTLat,eSacroTAcor,eLumbarPiRod,eLumbarPreDir,eLumbarPreLat,eLumbarPreAD) VALUES ( ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ?,  ? ) '

        #Ventana de Confirmación
        confirmation = QMessageBox.question(self, "Confirmación",
        "Hago constar que la información \n contenida en este documento es verdadera.",
        QMessageBox.Cancel | QMessageBox.Ok )
        if confirmation == QMessageBox.Ok:
            # Insertando Datos a la base de datos
            self.insertInto(dataBase,connectDB,sql,values)
            self.clearFormRegistre()
            print('Create Regisre')
            # Ir al inicio
            self.toolBox.setCurrentIndex(2)
            print(values)
        else:
            #Borrar Datos del form
            pass

    def showById(self):
        global dataBase, connectDB
        bandera = True
        register = self.iBuscarName.text()
        # Busquda por nombre, Descomentar
        sql = 'SELECT * FROM users WHERE name = ' +"'"+register +"'"

        # Busqueda por Id, folio, Descomenar
        # sql = 'SELECT * FROM users WHERE name = ' +register
        data = self.selectId(dataBase,connectDB,sql)
        try:
            if data[0]:
                bandera = False
                self.viewDataForm(data)
            else:
                print('Introduzca')
        except:
            if  bandera:
                confirmation = QMessageBox.question(self, "Aviso",
                "Registro No Encontrado.",
                QMessageBox.Ok )
                self.clearForm()

    def updateId(self):
        global dataBase, connectDB
        id = self.iId.text()
        # self.toolBox.setCurrentIndex(2)
        if id:

            print('actualizar')
            sql = self.getFormDataToUpdate()
            dataBase.execute(sql)
            connectDB.commit()
            confirmation = QMessageBox.question(self, "Aviso",
            "Registro Actualizado.",
            QMessageBox.Ok )
            
        else:
            confirmation = QMessageBox.question(self, "Aviso",
            "No hay registro que editar. \n Busque un registro.",
            QMessageBox.Ok )
        pass

    def deleteById(self):
        global dataBase, connectDB
        id = self.iId.text()
        name = self.iName_3.text()
        #Ventana de Confirmación
        if id:
            confirmation = QMessageBox.question(self, "Confirmación",
            f"Eliminar Registro de: { name}",
            QMessageBox.Cancel | QMessageBox.Ok )
            if confirmation == QMessageBox.Ok:
                # Delete Datos a la base de datos
                sql = 'DELETE FROM users WHERE id = ' + id
                dataBase.execute(sql)
                connectDB.commit()
                self.clearForm()
                self.bBuscar.setText('')
                confirmation = QMessageBox.question(self, "Aviso",
                "Registro Eliminado.",
                QMessageBox.Ok )
                # Ir al inicio
                self.toolBox.setCurrentIndex(2)
                print('Delete Registre')
            else:
                self.clearForm()
                pass
        else:
            confirmation = QMessageBox.question(self, "Aviso",
            "No hay registro que eliminar. \n Busque un registro.",
            QMessageBox.Ok )

        pass



    def insertInto(self,dataBase,connectDB,sql,values):
        dataBase.execute(sql,values)
        connectDB.commit()
        pass

    def selectId(self,dataBase,connectDB,sql):
        dataBase.execute(sql)
        data = dataBase.fetchone()
        return data
        pass

    def getDataForm(self):
        name = self.iName.text()
        edad = self.iEdad.text()
        genero = self.iGenero.currentText()
        fecha = self.iFecha.text()
        peso = self.iPeso.value()
        talla = self.iTalla.value()
        hora = self.iHora.text()
        areaTrabajo = self.iAreaTrabajo.text()
        tiempoLabora = self.iTiempoLabor.text()
        habitos = self.iHabitos.text()
        actividad = self.iActividad.text()
        tiempoRiesgo = self.iTiempoRiesgo.text()
        medicamento = self.iMedicamento.text()
        dolorMano = self.iDolorMano.isChecked()
        dolorMano2 = self.iDolorManoDer.isChecked()
        dolorMano3 = self.iDolorManoIzq.isChecked()
        dolorMano4 = self.iDolorManoInt.isChecked()
        dolorMano5 = self.iDolorManoFcia.isChecked()
        dolorMano6 = self.iDolorManoLocal.isChecked()
        dolorMano7 = self.iDolorManoIrrad.isChecked()

        dolorCuello = self.iDolorCuello.isChecked()
        dolorCuello2 = self.iDolorCuelloDer.isChecked()
        dolorCuello3 = self.iDolorCuelloIzq.isChecked()
        dolorCuello4 = self.iDolorCuelloInt.isChecked()
        dolorCuello5 = self.iDolorCuelloFcia.isChecked()
        dolorCuello6 = self.iDolorCuelloLocal.isChecked()
        dolorCuello7 = self.iDolorCuelloIrrad.isChecked()

        dolorHombro = self.iDolorHombro.isChecked()
        dolorHombro2 = self.iDolorHombroDer.isChecked()
        dolorHombro3 = self.iDolorHombroIzq.isChecked()
        dolorHombro4 = self.iDolorHombroInt.isChecked()
        dolorHombro5 = self.iDolorHombroFcia.isChecked()
        dolorHombro6 = self.iDolorHombroLocal.isChecked()
        dolorHombro7 = self.iDolorHombroIrrad.isChecked()

        dolorEspalda = self.iDolorEspalda.isChecked()
        dolorEspalda2 = self.iDolorEspaldaDer.isChecked()
        dolorEspalda3 = self.iDolorEspaldaIzq.isChecked()
        dolorEspalda4 = self.iDolorEspaldaInt.isChecked()
        dolorEspalda5 = self.iDolorEspaldaFcia.isChecked()
        dolorEspalda6 = self.iDolorEspaldaLocal.isChecked()
        dolorEspalda7 = self.iDolorEspaldaIrrad.isChecked()

        adormeMano = self.iAdormeManos.isChecked()
        adormeMano2 = self.iAdormeManosDer.isChecked()
        adormeMano3 = self.iAdormeManosIzq.isChecked()
        adormeMano4 = self.iAdormeManosInt.isChecked()
        adormeMano5 = self.iAdormeManosFcia.isChecked()
        adormeMano6 = self.iAdormeManosLocal.isChecked()
        adormeMano7 = self.iAdormeManosIrrad.isChecked()

        dismiMovMano = self.iDismiManos.isChecked()
        dismiMovMano2 = self.iDismiManos_2.isChecked()
        dismiMovMano3 = self.iDismiManosIzq.isChecked()
        dismiMovMano4 = self.iDismiManosInt.isChecked()
        dismiMovMano5 = self.iDismiManosFcia.isChecked()
        dismiMovMano6 = self.iDismiManosLocal.isChecked()
        dismiMovMano7 = self.iDismiManosIrrad.isChecked()

        perdidaFuMano = self.iPerdidaManos.isChecked()
        perdidaFuMano2 = self.iPerdidaManosDer.isChecked()
        perdidaFuMano3 = self.iPerdidaManosIzq.isChecked()
        perdidaFuMano4 = self.iPerdidaManosInt.isChecked()
        perdidaFuMano5 = self.iPerdidaManosFcia.isChecked()
        perdidaFuMano6 = self.iPerdidaManosLocal.isChecked()
        perdidaFuMano7 = self.iPerdidaManosIrrad.isChecked()

        torpeMano = self.iTorpezaMano.isChecked()
        torpeMano2 = self.iTorpezaManoDer.isChecked()
        torpeMano3 = self.iTorpezaManoIzq.isChecked()
        torpeMano4 = self.iTorpezaManoInt.isChecked()
        torpeMano5 = self.iTorpezaManoFcia.isChecked()
        torpeMano6 = self.iTorpezaManoLocal.isChecked()
        torpeMano7 = self.iTorpezaManoIrrad.isChecked()

        senExMano = self.iSensaMano.isChecked()
        senExMano2 = self.iSensaManoDer.isChecked()
        senExMano3 = self.iSensaManoIzq.isChecked()
        senExMano4 = self.iSensaManoInt.isChecked()
        senExMano5 = self.iSensaManoFcia.isChecked()
        senExMano6 = self.iSensaManoLocal.isChecked()
        senExMano7 = self.iSensaManoIrrad.isChecked()

        otrosMole = self.iOtroMolestia.text()

        obserDefor = self.iExObDeforSi.isChecked()
        obserInf = self.iExObInflaSi.isChecked()
        obserAtro = self.iExObAtroSi.isChecked()
        obserCam = self.iExObColoSi.isChecked()


        dmMusBrazoDer = self.iExDMusBrazoDer.value()
        dmMusBrazoIzq = self.iExDMusBrazoIzq.value()

        dmMusAnBrazoDer = self.iExDMusAnteBrazoDer.value()
        dmMusAnBrazoIzq = self.iExDMusAnteBrazoIzq.value()

        rMFleCD = self.iExRMovFlexCuelloDer.text()
        rMFleCI = self.iExRMovFlexCuelloIzq.text()
        rMFleHD = self.iExRMovFlexHombroDer.text()
        rMFleHI = self.iExRMovFlexHombroIzq.text()
        rMFleCoD = self.iExRMovFlexCodoDer.text()
        rMFleCoI = self.iExRMovFlexCodoIzq.text()
        rMFleMD = self.iExRMovFlexMunecaDer.text()
        rMFleMI = self.iExRMovFlexMunecaIzq.text()
        rMFleDD = self.iExRMovFlexDedoDer.text()
        rMFleDI = self.iExRMovFlexDedoIzq.text()

        rMExtCD = self.iExRMovExtCuelloDer.text()
        rMExtCI = self.iExRMovExtCuelloIzq.text()
        rMExtHD = self.iExRMovExtHombroDer.text()
        rMExtHI = self.iExRMovExtHombroIzq.text()
        rMExtCoD = self.iExRMovExtCodoDer.text()
        rMExtCoI = self.iExRMovExtCodoIzq.text()
        rMExtMD = self.iExRMovExtMunecaDer.text()
        rMExtMI = self.iExRMovExtMunecaIzq.text()
        rMExtDD = self.iExRMovExtDedoDer.text()
        rMExtDI = self.iExRMovExtDedoIzq.text()

        rMAdbCD = self.iExRMovAdbCuelloDer.text()
        rMAdbCI = self.iExRMovAdbCuelloIzq.text()
        rMAdbHD = self.iExRMovAdbHombroDer.text()
        rMAdbHI = self.iExRMovAdbHombroIzq.text()
        rMAdbCoD = self.iExRMovAdbCodoDer.text()
        rMAdbCoI = self.iExRMovAdbCodoIzq.text()
        rMAdbMD = self.iExRMovAdbMunecaDer.text()
        rMAdbMI = self.iExRMovAdbMunecaIzq.text()
        rMAdbDD = self.iExRMovAdbDedoDer.text()
        rMAdbDI = self.iExRMovAdbDedoIzq.text()

        rMAduCD = self.iExRMovAduCuelloDer.text()
        rMAduCI = self.iExRMovAduCuelloIzq.text()
        rMAduHD = self.iExRMovAduHombroDer.text()
        rMAduHI = self.iExRMovAduHombroIzq.text()
        rMAduCoD = self.iExRMovAduCodoDer.text()
        rMAduCoI = self.iExRMovAduCodoIzq.text()
        rMAduMD = self.iExRMovAduMunecaDer.text()
        rMAduMI = self.iExRMovAduMunecaIzq.text()
        rMAduDD = self.iExRMovAduDedoDer.text()
        rMAduDI = self.iExRMovAduDedoIzq.text()

        rMRotExtCD = self.iExRMovRotaExCuelloDer.text()
        rMRotExtCI = self.iExRMovRotaExCuelloIzq.text()
        rMRotExtHD = self.iExRMovRotaExHombroDer.text()
        rMRotExtHI = self.iExRMovRotaExHombroIzq.text()
        rMRotExtCoD = self.iExRMovRotaExCodoDer.text()
        rMRotExtCoI = self.iExRMovRotaExCodoIzq.text()
        rMRotExtMD = self.iExRMovRotaExMunecaDer.text()
        rMRotExtMI = self.iExRMovRotaExMunecaIzq.text()
        rMRotExtDD = self.iExRMovRotaExDedoDer.text()
        rMRotExtDI = self.iExRMovRotaExDedoIzq.text()

        rMRotInCD = self.iExRMovRotaIntCuelloDer.text()
        rMRotInCI = self.iExRMovRotaIntCuelloIzq.text()
        rMRotInHD = self.iExRMovRotaIntHombroDer.text()
        rMRotInHI = self.iExRMovRotaIntHombroIzq.text()
        rMRotInCoD = self.iExRMovRotaIntCodoDer.text()
        rMRotInCoI = self.iExRMovRotaIntCodoizq.text()
        rMRotInMD = self.iExRMovRotaIntMunecaDer.text()
        rMRotInMI = self.iExRMovRotaIntMunecaIzq.text()
        rMRotInDD = self.iExRMovRotaIntDedoDer.text()
        rMRotInDI = self.iExRMovRotaIntDedoIzq.text()

        rFMPrePalmaD = self.iExFMusPrePalmaDer.text()
        rFMPrePalmaI = self.iExFMusPrePalmaIzq.text()

        rFMPreDigD = self.iExFMusPreDigDer.text()
        rFMPreDigI = self.iExFMusPreDigIzq.text()

        rSenPMonoD = self.iExSenPMonoMDer.text()
        rSenPMonoI = self.iExSenPMonoMIzq.text()

        rSenVibroD = self.iExSenVibroMDer.text()
        rSenVibroI = self.iExSenVibroMIzq.text()

        rSenDisD = self.iExSenDTextuMDer.text()
        rSenDisI = self.iExSenDTextuMIzq.text()

        sESFlickD = self.iExSigEspSFlickDer.text()
        sESFlickI = self.iExSigEspSFlickIzq.text()

        sESPhallenD = self.iExSigEspSPhallenDer.text()
        sESPhallenI = self.iExSigEspSPhallenIzq.text()

        sESTinelD = self.iExSigEspSTinelDer.text()
        sESTinelI = self.iExSigEspSTinelIzq.text()

        sEsCirculoD = self.iExSigEspSCirculoDer.text()
        sEsCirculoI = self.iExSigEspSCirculoIzq.text()

        eCerviRes = self.iEvaCerviRespi.text()
        eCerviTRes = self.iEvaCerviTArCervi.text()
        eCerviOcc = self.iEvaCerviAOcc.text()
        eCerviC1 = self.iEvaCerviC1.text()
        eCerviC2 = self.iEvaCerviC2.text()
        eCerviC3 = self.iEvaCerviC3.text()
        eCerviC4 = self.iEvaCerviC4.text()
        eCerviC5 = self.iEvaCerviC5.text()
        eCerviC6 = self.iEvaCerviC6.text()
        eCerviC7 = self.iEvaCerviC7.text()

        eDorsPiRod = self.iEvaDorPinRod.text()
        eDorsPreDir = self.iEvaDorPreDirec.text()
        eDorsPreLat = self.iEvaDorPreLat.text()
        eDorsPreAD = self.iEvaDorPreAD.text()

        eIliacosTPie = self.iEvaIliaTArPie.text()
        eIliacosTPos = self.iEvaIliaTPos.text()
        eIliacosEias = self.iEvaIliaEias.text()
        eIliacosTAlar = self.iEvaIliaTAlarga.text()
        eIliacosTAcor = self.iEvaIliaTAcor.text()

        eSacroTArSen = self.iEvaSacroTArSentado.text()
        eSacroTRot = self.iEvaSacroTRota.text()
        eSacroTLat = self.iEvaSacroTLater.text()
        eSacroTAcor = self.iEvaSacroTAcor.text()

        eLumbarPiRod = self.iEvaLumbarPinRoda.text()
        eLumbarPreDir = self.iEvaLumbarPreDirec.text()
        eLumbarPreLat = self.iEvaLumbarPreLater.text()
        eLumbarPreAD = self.iEvaLumbarPreAD.text()

        values = ( name
            ,edad
            ,genero
            ,fecha
            ,peso
            ,talla
            ,hora
            ,areaTrabajo
            ,tiempoLabora
            ,habitos
            ,actividad
            ,tiempoRiesgo
            ,medicamento
            ,dolorMano
            ,dolorMano2
            ,dolorMano3
            ,dolorMano4
            ,dolorMano5
            ,dolorMano6
            ,dolorMano7
            ,dolorCuello
            ,dolorCuello2
            ,dolorCuello3
            ,dolorCuello4
            ,dolorCuello5
            ,dolorCuello6
            ,dolorCuello7
            ,dolorHombro
            ,dolorHombro2
            ,dolorHombro3
            ,dolorHombro4
            ,dolorHombro5
            ,dolorHombro6
            ,dolorHombro7
            ,dolorEspalda
            ,dolorEspalda2
            ,dolorEspalda3
            ,dolorEspalda4
            ,dolorEspalda5
            ,dolorEspalda6
            ,dolorEspalda7
            ,adormeMano
            ,adormeMano2
            ,adormeMano3
            ,adormeMano4
            ,adormeMano5
            ,adormeMano6
            ,adormeMano7
            ,dismiMovMano
            ,dismiMovMano2
            ,dismiMovMano3
            ,dismiMovMano4
            ,dismiMovMano5
            ,dismiMovMano6
            ,dismiMovMano7
            ,perdidaFuMano
            ,perdidaFuMano2
            ,perdidaFuMano3
            ,perdidaFuMano4
            ,perdidaFuMano5
            ,perdidaFuMano6
            ,perdidaFuMano7
            ,torpeMano
            ,torpeMano2
            ,torpeMano3
            ,torpeMano4
            ,torpeMano5
            ,torpeMano6
            ,torpeMano7
            ,senExMano
            ,senExMano2
            ,senExMano3
            ,senExMano4
            ,senExMano5
            ,senExMano6
            ,senExMano7
            ,otrosMole
            ,obserDefor
            ,obserInf
            ,obserAtro
            ,obserCam
            ,dmMusBrazoDer
            ,dmMusBrazoIzq
            ,dmMusAnBrazoDer
            ,dmMusAnBrazoIzq
            ,rMFleCD
            ,rMFleCI
            ,rMFleHD
            ,rMFleHI
            ,rMFleCoD
            ,rMFleCoI
            ,rMFleMD
            ,rMFleMI
            ,rMFleDD
            ,rMFleDI
            ,rMExtCD
            ,rMExtCI
            ,rMExtHD
            ,rMExtHI
            ,rMExtCoD
            ,rMExtCoI
            ,rMExtMD
            ,rMExtMI
            ,rMExtDD
            ,rMExtDI
            ,rMAdbCD
            ,rMAdbCI
            ,rMAdbHD
            ,rMAdbHI
            ,rMAdbCoD
            ,rMAdbCoI
            ,rMAdbMD
            ,rMAdbMI
            ,rMAdbDD
            ,rMAdbDI
            ,rMAduCD
            ,rMAduCI
            ,rMAduHD
            ,rMAduHI
            ,rMAduCoD
            ,rMAduCoI
            ,rMAduMD
            ,rMAduMI
            ,rMAduDD
            ,rMAduDI
            ,rMRotExtCD
            ,rMRotExtCI
            ,rMRotExtHD
            ,rMRotExtHI
            ,rMRotExtCoD
            ,rMRotExtCoI
            ,rMRotExtMD
            ,rMRotExtMI
            ,rMRotExtDD
            ,rMRotExtDI
            ,rMRotInCD
            ,rMRotInCI
            ,rMRotInHD
            ,rMRotInHI
            ,rMRotInCoD
            ,rMRotInCoI
            ,rMRotInMD
            ,rMRotInMI
            ,rMRotInDD
            ,rMRotInDI
            ,rFMPrePalmaD
            ,rFMPrePalmaI
            ,rFMPreDigD
            ,rFMPreDigI
            ,rSenPMonoD
            ,rSenPMonoI
            ,rSenVibroD
            ,rSenVibroI
            ,rSenDisD
            ,rSenDisI
            ,sESFlickD
            ,sESFlickI
            ,sESPhallenD
            ,sESPhallenI
            ,sESTinelD
            ,sESTinelI
            ,sEsCirculoD
            ,sEsCirculoI
            ,eCerviRes
            ,eCerviTRes
            ,eCerviOcc
            ,eCerviC1
            ,eCerviC2
            ,eCerviC3
            ,eCerviC4
            ,eCerviC5
            ,eCerviC6
            ,eCerviC7
            ,eDorsPiRod
            ,eDorsPreDir
            ,eDorsPreLat
            ,eDorsPreAD
            ,eIliacosTPie
            ,eIliacosTPos
            ,eIliacosEias
            ,eIliacosTAlar
            ,eIliacosTAcor
            ,eSacroTArSen
            ,eSacroTRot
            ,eSacroTLat
            ,eSacroTAcor
            ,eLumbarPiRod
            ,eLumbarPreDir
            ,eLumbarPreLat
            ,eLumbarPreAD )
        return values

    def str2bool(self,v):
        return str(v).lower() in ("1")

    def viewDataForm(self,data):
        self.iId.setText(str(data[0]))
        self.iName_3.setText(data[1])
        self.iEdad_3.setText(data[2])
        aux = self.iGenero_3.findText(data[3])
        self.iGenero_3.setCurrentIndex(aux)
        self.inpFecha.setText(data[4])
        self.inpPeso.setText(data[5])
        self.iTalla_3.setValue(int(data[6]))
        self.inpHora.setText(data[7])
        self.iAreaTrabajo_3.setText(data[8])
        self.iTiempoLabor_3.setValue(int(data[9]))
        self.iHabitos_3.setText(data[10])
        self.iActividad_3.setText(data[11])
        self.iTiempoRiesgo_3.setValue(int(data[12]))
        self.iMedicamento_3.setText(data[13])
        self.iDolorMano_3.setChecked( self.str2bool(data[14]) )
        self.iDolorManoDer_3.setChecked(self.str2bool(data[15]))
        self.iDolorManoIzq_3.setChecked(self.str2bool(data[16]))
        self.iDolorManoInt_3.setChecked(self.str2bool(data[17]))
        self.iDolorManoFcia_3.setChecked(self.str2bool(data[18]))
        self.iDolorManoLocal_3.setChecked(self.str2bool(data[19]))
        self.iDolorManoIrrad_3.setChecked(self.str2bool(data[20]))
        self.iDolorCuello_3.setChecked(self.str2bool(data[21]))
        self.iDolorCuelloDer_3.setChecked(self.str2bool(data[22]))
        self.iDolorCuelloIzq_3.setChecked(self.str2bool(data[23]))
        self.iDolorCuelloInt_3.setChecked(self.str2bool(data[24]))
        self.iDolorCuelloFcia_3.setChecked(self.str2bool(data[25]))
        self.iDolorCuelloLocal_3.setChecked(self.str2bool(data[26]))
        self.iDolorCuelloIrrad_3.setChecked(self.str2bool(data[27]))
        self.iDolorHombro_3.setChecked(self.str2bool(data[28]))
        self.iDolorHombroDer_3.setChecked(self.str2bool(data[29]))
        self.iDolorHombroIzq_3.setChecked(self.str2bool(data[30]))
        self.iDolorHombroInt_3.setChecked(self.str2bool(data[31]))
        self.iDolorHombroFcia_3.setChecked(self.str2bool(data[32]))
        self.iDolorHombroLocal_3.setChecked(self.str2bool(data[33]))
        self.iDolorHombroIrrad_3.setChecked(self.str2bool(data[34]))
        self.iDolorEspalda_3.setChecked(self.str2bool(data[35]))
        self.iDolorEspaldaDer_3.setChecked(self.str2bool(data[36]))
        self.iDolorEspaldaIzq_3.setChecked(self.str2bool(data[37]))
        self.iDolorEspaldaInt_3.setChecked(self.str2bool(data[38]))
        self.iDolorEspaldaFcia_3.setChecked(self.str2bool(data[39]))
        self.iDolorEspaldaLocal_3.setChecked(self.str2bool(data[40]))
        self.iDolorEspaldaIrrad_3.setChecked(self.str2bool(data[41]))

        self.iAdormeManos_3.setChecked(self.str2bool(data[42]))
        self.iAdormeManosDer_3.setChecked(self.str2bool(data[43]))
        self.iAdormeManosIzq_3.setChecked(self.str2bool(data[44]))
        self.iAdormeManosInt_3.setChecked(self.str2bool(data[45]))
        self.iAdormeManosFcia_3.setChecked(self.str2bool(data[46]))
        self.iAdormeManosLocal_3.setChecked(self.str2bool(data[47]))
        self.iAdormeManosIrrad_3.setChecked(self.str2bool(data[48]))

        self.iDismiManos_6.setChecked(self.str2bool(data[49]))
        self.iDismiManos_5.setChecked(self.str2bool(data[50]))
        self.iDismiManosIzq_3.setChecked(self.str2bool(data[51]))
        self.iDismiManosInt_3.setChecked(self.str2bool(data[52]))
        self.iDismiManosFcia_3.setChecked(self.str2bool(data[53]))
        self.iDismiManosLocal_3.setChecked(self.str2bool(data[54]))
        self.iDismiManosIrrad_3.setChecked(self.str2bool(data[55]))

        self.iPerdidaManos_3.setChecked(self.str2bool(data[56]))
        self.iPerdidaManosDer_3.setChecked(self.str2bool(data[57]))
        self.iPerdidaManosIzq_3.setChecked(self.str2bool(data[58]))
        self.iPerdidaManosInt_3.setChecked(self.str2bool(data[59]))
        self.iPerdidaManosFcia_3.setChecked(self.str2bool(data[60]))
        self.iPerdidaManosLocal_3.setChecked(self.str2bool(data[61]))
        self.iPerdidaManosIrrad_3.setChecked(self.str2bool(data[62]))

        self.iTorpezaMano_3.setChecked(self.str2bool(data[63]))
        self.iTorpezaManoDer_3.setChecked(self.str2bool(data[64]))
        self.iTorpezaManoIzq_3.setChecked(self.str2bool(data[65]))
        self.iTorpezaManoInt_3.setChecked(self.str2bool(data[66]))
        self.iTorpezaManoFcia_3.setChecked(self.str2bool(data[67]))
        self.iTorpezaManoLocal_3.setChecked(self.str2bool(data[68]))
        self.iTorpezaManoIrrad_3.setChecked(self.str2bool(data[69]))

        self.iSensaMano_3.setChecked(self.str2bool(data[70]))
        self.iSensaManoDer_3.setChecked(self.str2bool(data[71]))
        self.iSensaManoIzq_3.setChecked(self.str2bool(data[72]))
        self.iSensaManoInt_3.setChecked(self.str2bool(data[73]))
        self.iSensaManoFcia_3.setChecked(self.str2bool(data[74]))
        self.iSensaManoLocal_3.setChecked(self.str2bool(data[75]))
        self.iSensaManoIrrad_3.setChecked(self.str2bool(data[76]))

        self.iOtroMolestia_3.setText(data[77])

        self.iExObDeforSi_3.setChecked(self.str2bool(data[78]))
        self.iExObInflaSi_3.setChecked(self.str2bool(data[79]))
        self.iExObAtroSi_3.setChecked(self.str2bool(data[80]))
        self.iExObColoSi_5.setChecked(self.str2bool(data[81]))


        self.iExDMusBrazoDer_3.setValue(float(data[82]))
        self.iExDMusBrazoIzq_3.setValue(float(data[83]))

        self.iExDMusAnteBrazoDer_3.setValue(float(data[84]))
        self.iExDMusAnteBrazoIzq_3.setValue(float(data[85]))

        self.iExRMovFlexCuelloDer_3.setText(data[86])
        self.iExRMovFlexCuelloIzq_3.setText(data[87])
        self.iExRMovFlexHombroDer_3.setText(data[88])
        self.iExRMovFlexHombroIzq_3.setText(data[89])
        self.iExRMovFlexCodoDer_3.setText(data[90])
        self.iExRMovFlexCodoIzq_3.setText(data[91])
        self.iExRMovFlexMunecaDer_3.setText(data[92])
        self.iExRMovFlexMunecaIzq_3.setText(data[93])
        self.iExRMovFlexDedoDer_3.setText(data[94])
        self.iExRMovFlexDedoIzq_3.setText(data[95])

        self.iExRMovExtCuelloDer_3.setText(data[96])
        self.iExRMovExtCuelloIzq_3.setText(data[97])
        self.iExRMovExtHombroDer_3.setText(data[98])
        self.iExRMovExtHombroIzq_3.setText(data[99])
        self.iExRMovExtCodoDer_3.setText(data[100])
        self.iExRMovExtCodoIzq_3.setText(data[101])
        self.iExRMovExtMunecaDer_3.setText(data[102])
        self.iExRMovExtMunecaIzq_3.setText(data[103])
        self.iExRMovExtDedoDer_3.setText(data[104])
        self.iExRMovExtDedoIzq_3.setText(data[105])

        self.iExRMovAdbCuelloDer_3.setText(data[106])
        self.iExRMovAdbCuelloIzq_3.setText(data[107])
        self.iExRMovAdbHombroDer_3.setText(data[108])
        self.iExRMovAdbHombroIzq_3.setText(data[109])
        self.iExRMovAdbCodoDer_3.setText(data[110])
        self.iExRMovAdbCodoIzq_3.setText(data[111])
        self.iExRMovAdbMunecaDer_3.setText(data[112])
        self.iExRMovAdbMunecaIzq_3.setText(data[113])
        self.iExRMovAdbDedoDer_3.setText(data[114])
        self.iExRMovAdbDedoIzq_3.setText(data[115])

        self.iExRMovAduCuelloDer_3.setText(data[116])
        self.iExRMovAduCuelloIzq_3.setText(data[117])
        self.iExRMovAduHombroDer_3.setText(data[118])
        self.iExRMovAduHombroIzq_3.setText(data[119])
        self.iExRMovAduCodoDer_3.setText(data[120])
        self.iExRMovAduCodoIzq_3.setText(data[121])
        self.iExRMovAduMunecaDer_3.setText(data[122])
        self.iExRMovAduMunecaIzq_3.setText(data[123])
        self.iExRMovAduDedoDer_3.setText(data[124])
        self.iExRMovAduDedoIzq_3.setText(data[125])

        self.iExRMovRotaExCuelloDer_3.setText(data[126])
        self.iExRMovRotaExCuelloIzq_3.setText(data[127])
        self.iExRMovRotaExHombroDer_3.setText(data[128])
        self.iExRMovRotaExHombroIzq_3.setText(data[129])
        self.iExRMovRotaExCodoDer_3.setText(data[130])
        self.iExRMovRotaExCodoIzq_3.setText(data[131])
        self.iExRMovRotaExMunecaDer_3.setText(data[132])
        self.iExRMovRotaExMunecaIzq_3.setText(data[133])
        self.iExRMovRotaExDedoDer_3.setText(data[134])
        self.iExRMovRotaExDedoIzq_3.setText(data[135])

        self.iExRMovRotaIntCuelloDer_3.setText(data[136])
        self.iExRMovRotaIntCuelloIzq_3.setText(data[137])
        self.iExRMovRotaIntHombroDer_3.setText(data[138])
        self.iExRMovRotaIntHombroIzq_3.setText(data[139])
        self.iExRMovRotaIntCodoDer_3.setText(data[140])
        self.iExRMovRotaIntCodoizq_3.setText(data[141])
        self.iExRMovRotaIntMunecaDer_3.setText(data[142])
        self.iExRMovRotaIntMunecaIzq_3.setText(data[143])
        self.iExRMovRotaIntDedoDer_3.setText(data[144])
        self.iExRMovRotaIntDedoIzq_3.setText(data[145])

        self.iExFMusPrePalmaDer_3.setText(data[146])
        self.iExFMusPrePalmaIzq_3.setText(data[147])

        self.iExFMusPreDigDer_3.setText(data[148])
        self.iExFMusPreDigIzq_3.setText(data[149])

        self.iExSenPMonoMDer_3.setText(data[150])
        self.iExSenPMonoMIzq_3.setText(data[151])

        self.iExSenVibroMDer_3.setText(data[152])
        self.iExSenVibroMIzq_3.setText(data[153])

        self.iExSenDTextuMDer_3.setText(data[154])
        self.iExSenDTextuMIzq_3.setText(data[155])

        self.iExSigEspSFlickDer_3.setText(data[156])
        self.iExSigEspSFlickIzq_3.setText(data[157])

        self.iExSigEspSPhallenDer_3.setText(data[158])
        self.iExSigEspSPhallenIzq_3.setText(data[159])

        self.iExSigEspSTinelDer_3.setText(data[160])
        self.iExSigEspSTinelIzq_3.setText(data[161])

        self.iExSigEspSCirculoDer_3.setText(data[162])
        self.iExSigEspSCirculoIzq_3.setText(data[163])

        self.iEvaCerviRespi_3.setText(data[164])
        self.iEvaCerviTArCervi_3.setText(data[165])
        self.iEvaCerviAOcc_3.setText(data[166])
        self.iEvaCerviC1_3.setText(data[167])
        self.iEvaCerviC2_3.setText(data[168])
        self.iEvaCerviC3_3.setText(data[169])
        self.iEvaCerviC4_3.setText(data[170])
        self.iEvaCerviC5_3.setText(data[171])
        self.iEvaCerviC6_3.setText(data[172])
        self.iEvaCerviC7_3.setText(data[173])

        self.iEvaDorPinRod_3.setText(data[174])
        self.iEvaDorPreDirec_3.setText(data[175])
        self.iEvaDorPreLat_3.setText(data[176])
        self.iEvaDorPreAD_3.setText(data[177])

        self.iEvaIliaTArPie_3.setText(data[178])
        self.iEvaIliaTPos_3.setText(data[179])
        self.iEvaIliaEias_3.setText(data[180])
        self.iEvaIliaTAlarga_3.setText(data[181])
        self.iEvaIliaTAcor_3.setText(data[182])

        self.iEvaSacroTArSentado_3.setText(data[183])
        self.iEvaSacroTRota_3.setText(data[184])
        self.iEvaSacroTLater_3.setText(data[185])
        self.iEvaSacroTAcor_3.setText(data[186])

        self.iEvaLumbarPinRoda_3.setText(data[187])
        self.iEvaLumbarPreDirec_3.setText(data[188])
        self.iEvaLumbarPreLater_3.setText(data[189])
        self.iEvaLumbarPreAD_3.setText(data[190])

    def clearForm(self):
        self.iId .setText('')
        self.iName_3.setText('')
        self.iEdad_3.setText('')
        # aux = self.iGenero_3.findText(None)
        self.iGenero_3.setCurrentIndex(0)
        self.inpFecha.setText('')
        self.inpPeso.setText('')
        self.iTalla_3.setValue(0)
        self.inpHora.setText('')
        self.iAreaTrabajo_3.setText('')
        self.iTiempoLabor_3.setValue(0)
        self.iHabitos_3.setText('')
        self.iActividad_3.setText('')
        self.iTiempoRiesgo_3.setValue(0)
        self.iMedicamento_3.setText('')
        self.iDolorMano_3.setChecked(False)
        self.iDolorManoDer_3.setChecked(False)
        self.iDolorManoIzq_3.setChecked(False)
        self.iDolorManoInt_3.setChecked(False)
        self.iDolorManoFcia_3.setChecked(False)
        self.iDolorManoLocal_3.setChecked(False)
        self.iDolorManoIrrad_3.setChecked(False)
        self.iDolorCuello_3.setChecked(False)
        self.iDolorCuelloDer_3.setChecked(False)
        self.iDolorCuelloIzq_3.setChecked(False)
        self.iDolorCuelloInt_3.setChecked(False)
        self.iDolorCuelloFcia_3.setChecked(False)
        self.iDolorCuelloLocal_3.setChecked(False)
        self.iDolorCuelloIrrad_3.setChecked(False)
        self.iDolorHombro_3.setChecked(False)
        self.iDolorHombroDer_3.setChecked(False)
        self.iDolorHombroIzq_3.setChecked(False)
        self.iDolorHombroInt_3.setChecked(False)
        self.iDolorHombroFcia_3.setChecked(False)
        self.iDolorHombroLocal_3.setChecked(False)
        self.iDolorHombroIrrad_3.setChecked(False)
        self.iDolorEspalda_3.setChecked(False)
        self.iDolorEspaldaDer_3.setChecked(False)
        self.iDolorEspaldaIzq_3.setChecked(False)
        self.iDolorEspaldaInt_3.setChecked(False)
        self.iDolorEspaldaFcia_3.setChecked(False)
        self.iDolorEspaldaLocal_3.setChecked(False)
        self.iDolorEspaldaIrrad_3.setChecked(False)

        self.iAdormeManos_3.setChecked(False)
        self.iAdormeManosDer_3.setChecked(False)
        self.iAdormeManosIzq_3.setChecked(False)
        self.iAdormeManosInt_3.setChecked(False)
        self.iAdormeManosFcia_3.setChecked(False)
        self.iAdormeManosLocal_3.setChecked(False)
        self.iAdormeManosIrrad_3.setChecked(False)

        self.iDismiManos_6.setChecked(False)
        self.iDismiManos_5.setChecked(False)
        self.iDismiManosIzq_3.setChecked(False)
        self.iDismiManosInt_3.setChecked(False)
        self.iDismiManosFcia_3.setChecked(False)
        self.iDismiManosLocal_3.setChecked(False)
        self.iDismiManosIrrad_3.setChecked(False)

        self.iPerdidaManos_3.setChecked(False)
        self.iPerdidaManosDer_3.setChecked(False)
        self.iPerdidaManosIzq_3.setChecked(False)
        self.iPerdidaManosInt_3.setChecked(False)
        self.iPerdidaManosFcia_3.setChecked(False)
        self.iPerdidaManosLocal_3.setChecked(False)
        self.iPerdidaManosIrrad_3.setChecked(False)

        self.iTorpezaMano_3.setChecked(False)
        self.iTorpezaManoDer_3.setChecked(False)
        self.iTorpezaManoIzq_3.setChecked(False)
        self.iTorpezaManoInt_3.setChecked(False)
        self.iTorpezaManoFcia_3.setChecked(False)
        self.iTorpezaManoLocal_3.setChecked(False)
        self.iTorpezaManoIrrad_3.setChecked(False)

        self.iSensaMano_3.setChecked(False)
        self.iSensaManoDer_3.setChecked(False)
        self.iSensaManoIzq_3.setChecked(False)
        self.iSensaManoInt_3.setChecked(False)
        self.iSensaManoFcia_3.setChecked(False)
        self.iSensaManoLocal_3.setChecked(False)
        self.iSensaManoIrrad_3.setChecked(False)

        self.iOtroMolestia_3.setText('')

        self.iExObDeforSi_3.setChecked(False)
        self.iExObInflaSi_3.setChecked(False)
        self.iExObAtroSi_3.setChecked(False)
        self.iExObColoSi_5.setChecked(False)


        self.iExDMusBrazoDer_3.setValue(0)
        self.iExDMusBrazoIzq_3.setValue(0)

        self.iExDMusAnteBrazoDer_3.setValue(0)
        self.iExDMusAnteBrazoIzq_3.setValue(0)

        self.iExRMovFlexCuelloDer_3.setText('')
        self.iExRMovFlexCuelloIzq_3.setText('')
        self.iExRMovFlexHombroDer_3.setText('')
        self.iExRMovFlexHombroIzq_3.setText('')
        self.iExRMovFlexCodoDer_3.setText('')
        self.iExRMovFlexCodoIzq_3.setText('')
        self.iExRMovFlexMunecaDer_3.setText('')
        self.iExRMovFlexMunecaIzq_3.setText('')
        self.iExRMovFlexDedoDer_3.setText('')
        self.iExRMovFlexDedoIzq_3.setText('')

        self.iExRMovExtCuelloDer_3.setText('')
        self.iExRMovExtCuelloIzq_3.setText('')
        self.iExRMovExtHombroDer_3.setText('')
        self.iExRMovExtHombroIzq_3.setText('')
        self.iExRMovExtCodoDer_3.setText('')
        self.iExRMovExtCodoIzq_3.setText('')
        self.iExRMovExtMunecaDer_3.setText('')
        self.iExRMovExtMunecaIzq_3.setText('')
        self.iExRMovExtDedoDer_3.setText('')
        self.iExRMovExtDedoIzq_3.setText('')

        self.iExRMovAdbCuelloDer_3.setText('')
        self.iExRMovAdbCuelloIzq_3.setText('')
        self.iExRMovAdbHombroDer_3.setText('')
        self.iExRMovAdbHombroIzq_3.setText('')
        self.iExRMovAdbCodoDer_3.setText('')
        self.iExRMovAdbCodoIzq_3.setText('')
        self.iExRMovAdbMunecaDer_3.setText('')
        self.iExRMovAdbMunecaIzq_3.setText('')
        self.iExRMovAdbDedoDer_3.setText('')
        self.iExRMovAdbDedoIzq_3.setText('')

        self.iExRMovAduCuelloDer_3.setText('')
        self.iExRMovAduCuelloIzq_3.setText('')
        self.iExRMovAduHombroDer_3.setText('')
        self.iExRMovAduHombroIzq_3.setText('')
        self.iExRMovAduCodoDer_3.setText('')
        self.iExRMovAduCodoIzq_3.setText('')
        self.iExRMovAduMunecaDer_3.setText('')
        self.iExRMovAduMunecaIzq_3.setText('')
        self.iExRMovAduDedoDer_3.setText('')
        self.iExRMovAduDedoIzq_3.setText('')

        self.iExRMovRotaExCuelloDer_3.setText('')
        self.iExRMovRotaExCuelloIzq_3.setText('')
        self.iExRMovRotaExHombroDer_3.setText('')
        self.iExRMovRotaExHombroIzq_3.setText('')
        self.iExRMovRotaExCodoDer_3.setText('')
        self.iExRMovRotaExCodoIzq_3.setText('')
        self.iExRMovRotaExMunecaDer_3.setText('')
        self.iExRMovRotaExMunecaIzq_3.setText('')
        self.iExRMovRotaExDedoDer_3.setText('')
        self.iExRMovRotaExDedoIzq_3.setText('')

        self.iExRMovRotaIntCuelloDer_3.setText('')
        self.iExRMovRotaIntCuelloIzq_3.setText('')
        self.iExRMovRotaIntHombroDer_3.setText('')
        self.iExRMovRotaIntHombroIzq_3.setText('')
        self.iExRMovRotaIntCodoDer_3.setText('')
        self.iExRMovRotaIntCodoizq_3.setText('')
        self.iExRMovRotaIntMunecaDer_3.setText('')
        self.iExRMovRotaIntMunecaIzq_3.setText('')
        self.iExRMovRotaIntDedoDer_3.setText('')
        self.iExRMovRotaIntDedoIzq_3.setText('')

        self.iExFMusPrePalmaDer_3.setText('')
        self.iExFMusPrePalmaIzq_3.setText('')

        self.iExFMusPreDigDer_3.setText('')
        self.iExFMusPreDigIzq_3.setText('')

        self.iExSenPMonoMDer_3.setText('')
        self.iExSenPMonoMIzq_3.setText('')

        self.iExSenVibroMDer_3.setText('')
        self.iExSenVibroMIzq_3.setText('')

        self.iExSenDTextuMDer_3.setText('')
        self.iExSenDTextuMIzq_3.setText('')

        self.iExSigEspSFlickDer_3.setText('')
        self.iExSigEspSFlickIzq_3.setText('')

        self.iExSigEspSPhallenDer_3.setText('')
        self.iExSigEspSPhallenIzq_3.setText('')

        self.iExSigEspSTinelDer_3.setText('')
        self.iExSigEspSTinelIzq_3.setText('')

        self.iExSigEspSCirculoDer_3.setText('')
        self.iExSigEspSCirculoIzq_3.setText('')

        self.iEvaCerviRespi_3.setText('')
        self.iEvaCerviTArCervi_3.setText('')
        self.iEvaCerviAOcc_3.setText('')
        self.iEvaCerviC1_3.setText('')
        self.iEvaCerviC2_3.setText('')
        self.iEvaCerviC3_3.setText('')
        self.iEvaCerviC4_3.setText('')
        self.iEvaCerviC5_3.setText('')
        self.iEvaCerviC6_3.setText('')
        self.iEvaCerviC7_3.setText('')

        self.iEvaDorPinRod_3.setText('')
        self.iEvaDorPreDirec_3.setText('')
        self.iEvaDorPreLat_3.setText('')
        self.iEvaDorPreAD_3.setText('')

        self.iEvaIliaTArPie_3.setText('')
        self.iEvaIliaTPos_3.setText('')
        self.iEvaIliaEias_3.setText('')
        self.iEvaIliaTAlarga_3.setText('')
        self.iEvaIliaTAcor_3.setText('')

        self.iEvaSacroTArSentado_3.setText('')
        self.iEvaSacroTRota_3.setText('')
        self.iEvaSacroTLater_3.setText('')
        self.iEvaSacroTAcor_3.setText('')

        self.iEvaLumbarPinRoda_3.setText('')
        self.iEvaLumbarPreDirec_3.setText('')
        self.iEvaLumbarPreLater_3.setText('')
        self.iEvaLumbarPreAD_3.setText('')

    def clearFormRegistre(self):
        self.iName.setText('')
        self.iEdad.setText('')
        # aux = self.iGenero.findText(None)
        self.iGenero.setCurrentIndex(0)
        self.inpFecha.setText('')
        self.inpPeso.setText('')
        self.iTalla.setValue(0)
        self.inpHora.setText('')
        self.iAreaTrabajo.setText('')
        self.iTiempoLabor.setValue(0)
        self.iHabitos.setText('')
        self.iActividad.setText('')
        self.iTiempoRiesgo.setValue(0)
        self.iMedicamento.setText('')
        self.iDolorMano.setChecked(False)
        self.iDolorManoDer.setChecked(False)
        self.iDolorManoIzq.setChecked(False)
        self.iDolorManoInt.setChecked(False)
        self.iDolorManoFcia.setChecked(False)
        self.iDolorManoLocal.setChecked(False)
        self.iDolorManoIrrad.setChecked(False)
        self.iDolorCuello.setChecked(False)
        self.iDolorCuelloDer.setChecked(False)
        self.iDolorCuelloIzq.setChecked(False)
        self.iDolorCuelloInt.setChecked(False)
        self.iDolorCuelloFcia.setChecked(False)
        self.iDolorCuelloLocal.setChecked(False)
        self.iDolorCuelloIrrad.setChecked(False)
        self.iDolorHombro.setChecked(False)
        self.iDolorHombroDer.setChecked(False)
        self.iDolorHombroIzq.setChecked(False)
        self.iDolorHombroInt.setChecked(False)
        self.iDolorHombroFcia.setChecked(False)
        self.iDolorHombroLocal.setChecked(False)
        self.iDolorHombroIrrad.setChecked(False)
        self.iDolorEspalda.setChecked(False)
        self.iDolorEspaldaDer.setChecked(False)
        self.iDolorEspaldaIzq.setChecked(False)
        self.iDolorEspaldaInt.setChecked(False)
        self.iDolorEspaldaFcia.setChecked(False)
        self.iDolorEspaldaLocal.setChecked(False)
        self.iDolorEspaldaIrrad.setChecked(False)

        self.iAdormeManos.setChecked(False)
        self.iAdormeManosDer.setChecked(False)
        self.iAdormeManosIzq.setChecked(False)
        self.iAdormeManosInt.setChecked(False)
        self.iAdormeManosFcia.setChecked(False)
        self.iAdormeManosLocal.setChecked(False)
        self.iAdormeManosIrrad.setChecked(False)

        self.iDismiManos.setChecked(False)
        self.iDismiManos.setChecked(False)
        self.iDismiManosIzq.setChecked(False)
        self.iDismiManosInt.setChecked(False)
        self.iDismiManosFcia.setChecked(False)
        self.iDismiManosLocal.setChecked(False)
        self.iDismiManosIrrad.setChecked(False)

        self.iPerdidaManos.setChecked(False)
        self.iPerdidaManosDer.setChecked(False)
        self.iPerdidaManosIzq.setChecked(False)
        self.iPerdidaManosInt.setChecked(False)
        self.iPerdidaManosFcia.setChecked(False)
        self.iPerdidaManosLocal.setChecked(False)
        self.iPerdidaManosIrrad.setChecked(False)

        self.iTorpezaMano.setChecked(False)
        self.iTorpezaManoDer.setChecked(False)
        self.iTorpezaManoIzq.setChecked(False)
        self.iTorpezaManoInt.setChecked(False)
        self.iTorpezaManoFcia.setChecked(False)
        self.iTorpezaManoLocal.setChecked(False)
        self.iTorpezaManoIrrad.setChecked(False)

        self.iSensaMano.setChecked(False)
        self.iSensaManoDer.setChecked(False)
        self.iSensaManoIzq.setChecked(False)
        self.iSensaManoInt.setChecked(False)
        self.iSensaManoFcia.setChecked(False)
        self.iSensaManoLocal.setChecked(False)
        self.iSensaManoIrrad.setChecked(False)

        self.iOtroMolestia.setText('')

        self.iExObDeforSi.setChecked(False)
        self.iExObInflaSi.setChecked(False)
        self.iExObAtroSi.setChecked(False)
        self.iExObColoSi.setChecked(False)


        self.iExDMusBrazoDer.setValue(0)
        self.iExDMusBrazoIzq.setValue(0)

        self.iExDMusAnteBrazoDer.setValue(0)
        self.iExDMusAnteBrazoIzq.setValue(0)

        self.iExRMovFlexCuelloDer.setText('')
        self.iExRMovFlexCuelloIzq.setText('')
        self.iExRMovFlexHombroDer.setText('')
        self.iExRMovFlexHombroIzq.setText('')
        self.iExRMovFlexCodoDer.setText('')
        self.iExRMovFlexCodoIzq.setText('')
        self.iExRMovFlexMunecaDer.setText('')
        self.iExRMovFlexMunecaIzq.setText('')
        self.iExRMovFlexDedoDer.setText('')
        self.iExRMovFlexDedoIzq.setText('')

        self.iExRMovExtCuelloDer.setText('')
        self.iExRMovExtCuelloIzq.setText('')
        self.iExRMovExtHombroDer.setText('')
        self.iExRMovExtHombroIzq.setText('')
        self.iExRMovExtCodoDer.setText('')
        self.iExRMovExtCodoIzq.setText('')
        self.iExRMovExtMunecaDer.setText('')
        self.iExRMovExtMunecaIzq.setText('')
        self.iExRMovExtDedoDer.setText('')
        self.iExRMovExtDedoIzq.setText('')

        self.iExRMovAdbCuelloDer.setText('')
        self.iExRMovAdbCuelloIzq.setText('')
        self.iExRMovAdbHombroDer.setText('')
        self.iExRMovAdbHombroIzq.setText('')
        self.iExRMovAdbCodoDer.setText('')
        self.iExRMovAdbCodoIzq.setText('')
        self.iExRMovAdbMunecaDer.setText('')
        self.iExRMovAdbMunecaIzq.setText('')
        self.iExRMovAdbDedoDer.setText('')
        self.iExRMovAdbDedoIzq.setText('')

        self.iExRMovAduCuelloDer.setText('')
        self.iExRMovAduCuelloIzq.setText('')
        self.iExRMovAduHombroDer.setText('')
        self.iExRMovAduHombroIzq.setText('')
        self.iExRMovAduCodoDer.setText('')
        self.iExRMovAduCodoIzq.setText('')
        self.iExRMovAduMunecaDer.setText('')
        self.iExRMovAduMunecaIzq.setText('')
        self.iExRMovAduDedoDer.setText('')
        self.iExRMovAduDedoIzq.setText('')

        self.iExRMovRotaExCuelloDer.setText('')
        self.iExRMovRotaExCuelloIzq.setText('')
        self.iExRMovRotaExHombroDer.setText('')
        self.iExRMovRotaExHombroIzq.setText('')
        self.iExRMovRotaExCodoDer.setText('')
        self.iExRMovRotaExCodoIzq.setText('')
        self.iExRMovRotaExMunecaDer.setText('')
        self.iExRMovRotaExMunecaIzq.setText('')
        self.iExRMovRotaExDedoDer.setText('')
        self.iExRMovRotaExDedoIzq.setText('')

        self.iExRMovRotaIntCuelloDer.setText('')
        self.iExRMovRotaIntCuelloIzq.setText('')
        self.iExRMovRotaIntHombroDer.setText('')
        self.iExRMovRotaIntHombroIzq.setText('')
        self.iExRMovRotaIntCodoDer.setText('')
        self.iExRMovRotaIntCodoizq.setText('')
        self.iExRMovRotaIntMunecaDer.setText('')
        self.iExRMovRotaIntMunecaIzq.setText('')
        self.iExRMovRotaIntDedoDer.setText('')
        self.iExRMovRotaIntDedoIzq.setText('')

        self.iExFMusPrePalmaDer.setText('')
        self.iExFMusPrePalmaIzq.setText('')

        self.iExFMusPreDigDer.setText('')
        self.iExFMusPreDigIzq.setText('')

        self.iExSenPMonoMDer.setText('')
        self.iExSenPMonoMIzq.setText('')

        self.iExSenVibroMDer.setText('')
        self.iExSenVibroMIzq.setText('')

        self.iExSenDTextuMDer.setText('')
        self.iExSenDTextuMIzq.setText('')

        self.iExSigEspSFlickDer.setText('')
        self.iExSigEspSFlickIzq.setText('')

        self.iExSigEspSPhallenDer.setText('')
        self.iExSigEspSPhallenIzq.setText('')

        self.iExSigEspSTinelDer.setText('')
        self.iExSigEspSTinelIzq.setText('')

        self.iExSigEspSCirculoDer.setText('')
        self.iExSigEspSCirculoIzq.setText('')

        self.iEvaCerviRespi.setText('')
        self.iEvaCerviTArCervi.setText('')
        self.iEvaCerviAOcc.setText('')
        self.iEvaCerviC1.setText('')
        self.iEvaCerviC2.setText('')
        self.iEvaCerviC3.setText('')
        self.iEvaCerviC4.setText('')
        self.iEvaCerviC5.setText('')
        self.iEvaCerviC6.setText('')
        self.iEvaCerviC7.setText('')

        self.iEvaDorPinRod.setText('')
        self.iEvaDorPreDirec.setText('')
        self.iEvaDorPreLat.setText('')
        self.iEvaDorPreAD.setText('')

        self.iEvaIliaTArPie.setText('')
        self.iEvaIliaTPos.setText('')
        self.iEvaIliaEias.setText('')
        self.iEvaIliaTAlarga.setText('')
        self.iEvaIliaTAcor.setText('')

        self.iEvaSacroTArSentado.setText('')
        self.iEvaSacroTRota.setText('')
        self.iEvaSacroTLater.setText('')
        self.iEvaSacroTAcor.setText('')

        self.iEvaLumbarPinRoda.setText('')
        self.iEvaLumbarPreDirec.setText('')
        self.iEvaLumbarPreLater.setText('')
        self.iEvaLumbarPreAD.setText('')

    def getFormDataToUpdate(self):

        sql = f'''UPDATE users SET
        name = '{self.iName_3.text()}'
        ,edad = '{self.iEdad_3.text()}'
        ,genero = '{self.iGenero.currentText()}'
        ,fecha = '{self.inpFecha.text()}'
        ,peso = '{self.inpPeso.text()}'
        ,talla = '{self.iTalla_3.value()}'
        ,hora = '{self.inpHora.text()}'
        ,areaTrabajo = '{self.iAreaTrabajo_3.text()}'
        ,timpoLabora = '{self.iTiempoLabor_3.text()}'
        ,habitos = '{self.iHabitos_3.text()}'
        ,actividad = '{self.iActividad_3.text()}'
        ,tiempoRiesgo = '{self.iTiempoRiesgo_3.text()}'
        ,medicamento = '{self.iMedicamento_3.text()}'
        ,dolorMano = '{self.iDolorMano_3.isChecked()}'
        ,dolorManoDer = '{self.iDolorManoDer_3.isChecked()}'
        ,dolorManoIzq = '{self.iDolorManoIzq_3.isChecked()}'
        ,dolorManoInt = '{self.iDolorManoInt_3.isChecked()}'
        ,dolorManoFcia = '{self.iDolorManoFcia_3.isChecked()}'
        ,dolorManoLocal = '{self.iDolorManoLocal_3.isChecked()}'
        ,dolorManoIrrad = '{self.iDolorManoIrrad_3.isChecked()}'
        ,dolorCuello = '{self.iDolorCuello_3.isChecked()}'
        ,dolorCuello2 = '{self.iDolorCuelloDer_3.isChecked()}'
        ,dolorCuello3 = '{self.iDolorCuelloIzq_3.isChecked()}'
        ,dolorCuello4 = '{self.iDolorCuelloInt_3.isChecked()}'
        ,dolorCuello5 = '{self.iDolorCuelloFcia_3.isChecked()}'
        ,dolorCuello6 = '{self.iDolorCuelloLocal_3.isChecked()}'
        ,dolorCuello7 = '{self.iDolorCuelloIrrad_3.isChecked()}'
        ,dolorHombro = '{self.iDolorHombro_3.isChecked()}'
        ,dolorHombro2 = '{self.iDolorHombroDer_3.isChecked()}'
        ,dolorHombro3 = '{self.iDolorHombroIzq_3.isChecked()}'
        ,dolorHombro4 = '{self.iDolorHombroInt_3.isChecked()}'
        ,dolorHombro5 = '{self.iDolorHombroFcia_3.isChecked()}'
        ,dolorHombro6 = '{self.iDolorHombroLocal_3.isChecked()}'
        ,dolorHombro7 = '{self.iDolorHombroIrrad_3.isChecked()}'
        ,dolorEspalda = '{self.iDolorEspalda_3.isChecked()}'
        ,dolorEspalda2 = '{self.iDolorEspaldaDer_3.isChecked()}'
        ,dolorEspalda3 = '{self.iDolorEspaldaIzq_3.isChecked()}'
        ,dolorEspalda4 = '{self.iDolorEspaldaInt_3.isChecked()}'
        ,dolorEspalda5 = '{self.iDolorEspaldaFcia_3.isChecked()}'
        ,dolorEspalda6 = '{self.iDolorEspaldaLocal_3.isChecked()}'
        ,dolorEspalda7 = '{self.iDolorEspaldaIrrad_3.isChecked()}'
        ,adormeMano = '{self.iAdormeManos_3.isChecked()}'
        ,adormeMano2 = '{self.iAdormeManosDer_3.isChecked()}'
        ,adormeMano3 = '{self.iAdormeManosIzq_3.isChecked()}'
        ,adormeMano4 = '{self.iAdormeManosInt_3.isChecked()}'
        ,adormeMano5 = '{self.iAdormeManosFcia_3.isChecked()}'
        ,adormeMano6 = '{self.iAdormeManosLocal_3.isChecked()}'
        ,adormeMano7 = '{self.iAdormeManosIrrad_3.isChecked()}'
        ,dismiMovMano = '{self.iDismiManos_6.isChecked()}'
        ,dismiMovMano2 = '{self.iDismiManos_5.isChecked()}'
        ,dismiMovMano3 = '{self.iDismiManosIzq_3.isChecked()}'
        ,dismiMovMano4 = '{self.iDismiManosInt_3.isChecked()}'
        ,dismiMovMano5 = '{self.iDismiManosFcia_3.isChecked()}'
        ,dismiMovMano6 = '{self.iDismiManosLocal_3.isChecked()}'
        ,dismiMovMano7 = '{self.iDismiManosIrrad_3.isChecked()}'
        ,perdidaFuMano = '{self.iPerdidaManos_3.isChecked()}'
        ,perdidaFuMano2 = '{self.iPerdidaManosDer_3.isChecked()}'
        ,perdidaFuMano3 = '{self.iPerdidaManosIzq_3.isChecked()}'
        ,perdidaFuMano4 = '{self.iPerdidaManosInt_3.isChecked()}'
        ,perdidaFuMano5 = '{self.iPerdidaManosFcia_3.isChecked()}'
        ,perdidaFuMano6 = '{self.iPerdidaManosLocal_3.isChecked()}'
        ,perdidaFuMano7 = '{self.iPerdidaManosIrrad_3.isChecked()}'
        ,torpeMano = '{self.iTorpezaMano_3.isChecked()}'
        ,torpeMano2 = '{self.iTorpezaManoDer_3.isChecked()}'
        ,torpeMano3 = '{self.iTorpezaManoIzq_3.isChecked()}'
        ,torpeMano4 = '{self.iTorpezaManoInt_3.isChecked()}'
        ,torpeMano5 = '{self.iTorpezaManoFcia_3.isChecked()}'
        ,torpeMano6 = '{self.iTorpezaManoLocal_3.isChecked()}'
        ,torpeMano7 = '{self.iTorpezaManoIrrad_3.isChecked()}'
        ,senExMano = '{self.iSensaMano_3.isChecked()}'
        ,senExMano2 = '{self.iSensaManoDer_3.isChecked()}'
        ,senExMano3 = '{self.iSensaManoIzq_3.isChecked()}'
        ,senExMano4 = '{self.iSensaManoInt_3.isChecked()}'
        ,senExMano5 = '{self.iSensaManoFcia_3.isChecked()}'
        ,senExMano6 = '{self.iSensaManoLocal_3.isChecked()}'
        ,senExMano7 = '{self.iSensaManoIrrad_3.isChecked()}'
        ,otrosMole = '{self.iOtroMolestia_3.text()}'
        ,obserDefor = '{self.iExObDeforSi_3.isChecked()}'
        ,obserInf = '{self.iExObInflaSi_3.isChecked()}'
        ,obserAtro = '{self.iExObAtroSi_3.isChecked()}'
        ,obserCam = '{self.iExObColoSi_5.isChecked()}'
        ,dmMusBrazoDer = '{self.iExDMusBrazoDer.value()}'
        ,dmMusBrazoIzq = '{self.iExDMusBrazoIzq.value()}'
        ,dmMusAnBrazoDer = '{self.iExDMusAnteBrazoDer.value()}'
        ,dmMusAnBrazoIzq = '{self.iExDMusAnteBrazoIzq.value()}'
        ,rMFleCD = '{self.iExRMovFlexCuelloDer_3.text()}'
        ,rMFleCI = '{self.iExRMovFlexCuelloIzq_3.text()}'
        ,rMFleHD = '{self.iExRMovFlexHombroDer_3.text()}'
        ,rMFleHI = '{self.iExRMovFlexHombroIzq_3.text()}'
        ,rMFleCoD = '{self.iExRMovFlexCodoDer_3.text()}'
        ,rMFleCoI = '{self.iExRMovFlexCodoIzq_3.text()}'
        ,rMFleMD = '{self.iExRMovFlexMunecaDer_3.text()}'
        ,rMFleMI = '{self.iExRMovFlexMunecaIzq_3.text()}'
        ,rMFleDD = '{self.iExRMovFlexDedoDer_3.text()}'
        ,rMFleDI = '{self.iExRMovFlexDedoIzq_3.text()}'
        ,rMExtCD = '{self.iExRMovExtCuelloDer_3.text()}'
        ,rMExtCI = '{self.iExRMovExtCuelloIzq_3.text()}'
        ,rMExtHD = '{self.iExRMovExtHombroDer_3.text()}'
        ,rMExtHI = '{self.iExRMovExtHombroIzq_3.text()}'
        ,rMExtCoD = '{self.iExRMovExtCodoDer_3.text()}'
        ,rMExtCoI = '{self.iExRMovExtCodoIzq_3.text()}'
        ,rMExtMD = '{self.iExRMovExtMunecaDer_3.text()}'
        ,rMExtMI = '{self.iExRMovExtMunecaIzq_3.text()}'
        ,rMExtDD = '{self.iExRMovExtDedoDer_3.text()}'
        ,rMExtDI = '{self.iExRMovExtDedoIzq_3.text()}'
        ,rMAdbCD = '{self.iExRMovAdbCuelloDer_3.text()}'
        ,rMAdbCI = '{self.iExRMovAdbCuelloIzq_3.text()}'
        ,rMAdbHD = '{self.iExRMovAdbHombroDer_3.text()}'
        ,rMAdbHI = '{self.iExRMovAdbHombroIzq_3.text()}'
        ,rMAdbCoD = '{self.iExRMovAdbCodoDer_3.text()}'
        ,rMAdbCoI = '{self.iExRMovAdbCodoIzq_3.text()}'
        ,rMAdbMD = '{self.iExRMovAdbMunecaDer_3.text()}'
        ,rMAdbMI = '{self.iExRMovAdbMunecaIzq_3.text()}'
        ,rMAdbDD = '{self.iExRMovAdbDedoDer_3.text()}'
        ,rMAdbDI = '{self.iExRMovAdbDedoIzq_3.text()}'
        ,rMAduCD = '{self.iExRMovAduCuelloDer_3.text()}'
        ,rMAduCI = '{self.iExRMovAduCuelloIzq_3.text()}'
        ,rMAduHD = '{self.iExRMovAduHombroDer_3.text()}'
        ,rMAduHI = '{self.iExRMovAduHombroIzq_3.text()}'
        ,rMAduCoD = '{self.iExRMovAduCodoDer_3.text()}'
        ,rMAduCoI = '{self.iExRMovAduCodoIzq_3.text()}'
        ,rMAduMD = '{self.iExRMovAduMunecaDer_3.text()}'
        ,rMAduMI = '{self.iExRMovAduMunecaIzq_3.text()}'
        ,rMAduDD = '{self.iExRMovAduDedoDer_3.text()}'
        ,rMAduDI = '{self.iExRMovAduDedoIzq_3.text()}'
        ,rMRotExtCD = '{self.iExRMovRotaExCuelloDer_3.text()}'
        ,rMRotExtCI = '{self.iExRMovRotaExCuelloIzq_3.text()}'
        ,rMRotExtHD = '{self.iExRMovRotaExHombroDer_3.text()}'
        ,rMRotExtHI = '{self.iExRMovRotaExHombroIzq_3.text()}'
        ,rMRotExtCoD = '{self.iExRMovRotaExCodoDer_3.text()}'
        ,rMRotExtCoI = '{self.iExRMovRotaExCodoIzq_3.text()}'
        ,rMRotExtMD = '{self.iExRMovRotaExMunecaDer_3.text()}'
        ,rMRotExtMI = '{self.iExRMovRotaExMunecaIzq_3.text()}'
        ,rMRotExtDD = '{self.iExRMovRotaExDedoDer_3.text()}'
        ,rMRotExtDI = '{self.iExRMovRotaExDedoIzq_3.text()}'
        ,rMRotInCD = '{self.iExRMovRotaIntCuelloDer_3.text()}'
        ,rMRotInCI = '{self.iExRMovRotaIntCuelloIzq_3.text()}'
        ,rMRotInHD = '{self.iExRMovRotaIntHombroDer_3.text()}'
        ,rMRotInHI = '{self.iExRMovRotaIntHombroIzq_3.text()}'
        ,rMRotInCoD = '{self.iExRMovRotaIntCodoDer_3.text()}'
        ,rMRotInCoI = '{self.iExRMovRotaIntCodoizq_3.text()}'
        ,rMRotInMD = '{self.iExRMovRotaIntMunecaDer_3.text()}'
        ,rMRotInMI = '{self.iExRMovRotaIntMunecaIzq_3.text()}'
        ,rMRotInDD = '{self.iExRMovRotaIntDedoDer_3.text()}'
        ,rMRotInDI = '{self.iExRMovRotaIntDedoIzq_3.text()}'
        ,rFMPrePalmaD = '{self.iExFMusPrePalmaDer_3.text()}'
        ,rFMPrePalmaI = '{self.iExFMusPrePalmaIzq_3.text()}'
        ,rFMPreDigD = '{self.iExFMusPreDigDer_3.text()}'
        ,rFMPreDigI = '{self.iExFMusPreDigIzq_3.text()}'
        ,rSenPMonoD = '{self.iExSenPMonoMDer_3.text()}'
        ,rSenPMonoI = '{self.iExSenPMonoMIzq_3.text()}'
        ,rSenVibroD = '{self.iExSenVibroMDer_3.text()}'
        ,rSenVibroI = '{self.iExSenVibroMIzq_3.text()}'
        ,rSenDisD = '{self.iExSenDTextuMDer_3.text()}'
        ,rSenDisI = '{self.iExSenDTextuMIzq_3.text()}'
        ,sESFlickD = '{self.iExSigEspSFlickDer_3.text()}'
        ,sESFlickI = '{self.iExSigEspSFlickIzq_3.text()}'
        ,sESPhallenD = '{self.iExSigEspSPhallenDer_3.text()}'
        ,sESPhallenI = '{self.iExSigEspSPhallenIzq_3.text()}'
        ,sESTinelD = '{self.iExSigEspSTinelDer_3.text()}'
        ,sESTinelI = '{self.iExSigEspSTinelIzq_3.text()}'
        ,sEsCirculoD = '{self.iExSigEspSCirculoDer_3.text()}'
        ,sEsCirculoI = '{self.iExSigEspSCirculoIzq_3.text()}'
        ,eCerviRes = '{self.iEvaCerviRespi_3.text()}'
        ,eCerviTRes = '{self.iEvaCerviTArCervi_3.text()}'
        ,eCerviOcc = '{self.iEvaCerviAOcc_3.text()}'
        ,eCerviC1 = '{self.iEvaCerviC1_3.text()}'
        ,eCerviC2 = '{self.iEvaCerviC2_3.text()}'
        ,eCerviC3 = '{self.iEvaCerviC3_3.text()}'
        ,eCerviC4 = '{self.iEvaCerviC4_3.text()}'
        ,eCerviC5 = '{self.iEvaCerviC5_3.text()}'
        ,eCerviC6 = '{self.iEvaCerviC6_3.text()}'
        ,eCerviC7 = '{self.iEvaCerviC7_3.text()}'
        ,eDorsPiRod = '{self.iEvaDorPinRod_3.text()}'
        ,eDorsPreDir = '{self.iEvaDorPreDirec_3.text()}'
        ,eDorsPreLat = '{self.iEvaDorPreLat_3.text()}'
        ,eDorsPreAD = '{self.iEvaDorPreAD_3.text()}'
        ,eIliacosTPie = '{self.iEvaIliaTArPie_3.text()}'
        ,eIliacosTPos = '{self.iEvaIliaTPos_3.text()}'
        ,eIliacosEias = '{self.iEvaIliaEias_3.text()}'
        ,eIliacosTAlar = '{self.iEvaIliaTAlarga_3.text()}'
        ,eIliacosTAcor = '{self.iEvaIliaTAcor_3.text()}'
        ,eSacroTArSen = '{self.iEvaSacroTArSentado_3.text()}'
        ,eSacroTRot = '{self.iEvaSacroTRota_3.text()}'
        ,eSacroTLat = '{self.iEvaSacroTLater_3.text()}'
        ,eSacroTAcor = '{self.iEvaSacroTAcor_3.text()}'
        ,eLumbarPiRod = '{self.iEvaLumbarPinRoda_3.text()}'
        ,eLumbarPreDir = '{self.iEvaLumbarPreDirec_3.text()}'
        ,eLumbarPreLat = '{self.iEvaLumbarPreLater_3.text()}'
        ,eLumbarPreAD = '{self.iEvaLumbarPreAD_3.text()}' WHERE id = {self.iId.text()}'''

        return sql


    def connectionDataBase(self):
        try:
            # Establecer un objeto de la base datos. Hacer la coneccion a la base de datos
            connectDB = sqlite3.connect('dataBase.db')
            dataBase = connectDB.cursor()
            print('successful connection Data Base')
            return dataBase, connectDB
            pass
        except:
            print('Error Coneccion Base de Datos: ')
            pass
        # self.getDataFrom()

    def createTable(self,dataBase):
        dataBase.execute('CREATE TABLE users(id integer PRIMARY KEY, name text, edad text, genero text, fecha text, peso text, talla text, hora text, areaTrabajo text, timpoLabora text, habitos text, actividad text, tiempoRiesgo text, medicamento text, dolorMano text, dolorManoDer text, dolorManoIzq text, dolorManoInt text, dolorManoFcia text, dolorManoLocal text, dolorManoIrrad text, dolorCuello text, dolorCuello2 text, dolorCuello3 text, dolorCuello4 text, dolorCuello5 text, dolorCuello6 text, dolorCuello7 text, dolorHombro text, dolorHombro2 text, dolorHombro3 text, dolorHombro4 text, dolorHombro5 text, dolorHombro6 text, dolorHombro7 text, dolorEspalda text, dolorEspalda2 text, dolorEspalda3 text, dolorEspalda4 text, dolorEspalda5 text, dolorEspalda6 text, dolorEspalda7 text, adormeMano text, adormeMano2 text, adormeMano3 text, adormeMano4 text, adormeMano5 text, adormeMano6 text, adormeMano7 text, dismiMovMano text, dismiMovMano2 text, dismiMovMano3 text, dismiMovMano4 text, dismiMovMano5 text, dismiMovMano6 text, dismiMovMano7 text, perdidaFuMano text, perdidaFuMano2 text, perdidaFuMano3 text, perdidaFuMano4 text, perdidaFuMano5 text, perdidaFuMano6 text, perdidaFuMano7 text, torpeMano text, torpeMano2 text, torpeMano3 text, torpeMano4 text, torpeMano5 text, torpeMano6 text, torpeMano7 text, senExMano text, senExMano2 text, senExMano3 text, senExMano4 text, senExMano5 text, senExMano6 text, senExMano7 text, otrosMole text, obserDefor text, obserInf text, obserAtro text, obserCam text, dmMusBrazoDer text, dmMusBrazoIzq text, dmMusAnBrazoDer text, dmMusAnBrazoIzq text, rMFleCD text, rMFleCI text, rMFleHD text, rMFleHI text, rMFleCoD text, rMFleCoI text, rMFleMD text, rMFleMI text, rMFleDD text, rMFleDI text, rMExtCD text, rMExtCI text, rMExtHD text, rMExtHI text, rMExtCoD text, rMExtCoI text,  rMExtMD text, rMExtMI text, rMExtDD text, rMExtDI text, rMAdbCD text, rMAdbCI text, rMAdbHD text, rMAdbHI text, rMAdbCoD text, rMAdbCoI text, rMAdbMD text, rMAdbMI text, rMAdbDD text, rMAdbDI text, rMAduCD text, rMAduCI text, rMAduHD text, rMAduHI text, rMAduCoD text, rMAduCoI text, rMAduMD text, rMAduMI text, rMAduDD text, rMAduDI text, rMRotExtCD text, rMRotExtCI text, rMRotExtHD text, rMRotExtHI text, rMRotExtCoD text, rMRotExtCoI text, rMRotExtMD text, rMRotExtMI text, rMRotExtDD text, rMRotExtDI text, rMRotInCD text, rMRotInCI text, rMRotInHD text, rMRotInHI text, rMRotInCoD text, rMRotInCoI text, rMRotInMD text, rMRotInMI text, rMRotInDD text, rMRotInDI text, rFMPrePalmaD text, rFMPrePalmaI text, rFMPreDigD text, rFMPreDigI text, rSenPMonoD text, rSenPMonoI text, rSenVibroD text, rSenVibroI text, rSenDisD text, rSenDisI text, sESFlickD text, sESFlickI text, sESPhallenD text, sESPhallenI text, sESTinelD text, sESTinelI text, sESCirculoD text, sESCirculoI text, eCerviRes text, eCerviTRes text, eCerviOcc text, eCerviC1 text, eCerviC2 text, eCerviC3 text, eCerviC4 text, eCerviC5 text, eCerviC6 text, eCerviC7 text, eDorsPiRod text, eDorsPreDir text, eDorsPreLat text, eDorsPreAD text, eIliacosTPie text, eIliacosTPos text, eIliacosEias text, eIliacosTAlar text, eIliacosTAcor text, eSacroTArSen text, eSacroTRot text, eSacroTLat text, eSacroTAcor text, eLumbarPiRod text, eLumbarPreDir text, eLumbarPreLat text, eLumbarPreAD text)')
        print('Table Creado')
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

    pass