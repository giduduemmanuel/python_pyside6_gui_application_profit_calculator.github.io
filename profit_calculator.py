from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QGroupBox, QVBoxLayout, QMessageBox, QHBoxLayout, QLineEdit, QLabel
#from PySide6.QTGui import QFont
import pandas as pd
import sys

#create an empty list
maize_records = []
beans_records = []
millet_records = []

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #create the main window features
        self.setWindowTitle("Profit Calculator App/ Developed by Emmanuel Gidudu")
        self.setGeometry(100,100,1000,1000)

        #create the first layout, all these are for maize
        layout1 = QHBoxLayout()
        #create three inputbox to display information
        self.profit_input = QLineEdit()
        self.profit_input.setPlaceholderText("Profit here:")
        self.profit_input.setReadOnly(True)

        self.percent_profit_input = QLineEdit()
        self.percent_profit_input.setPlaceholderText("Percent Profit here:")
        self.percent_profit_input.setReadOnly(True)

        self.total_cost_price = QLineEdit()
        self.total_cost_price.setPlaceholderText("Total Cost price here:")
        self.total_cost_price.setReadOnly(True)

        self.total_selling_price = QLineEdit()
        self.total_selling_price.setPlaceholderText("Total selling price here:")
        self.total_selling_price.setReadOnly(True)

        #add all these widgets to the QHLayout
        layout1.addWidget(self.profit_input)
        layout1.addWidget(self.percent_profit_input)
        layout1.addWidget(self.total_cost_price)
        layout1.addWidget(self.total_selling_price)

        #create the second layouts
        layout2 = QHBoxLayout()
        #create the inputbox to accept the cost price
        self.cost_price_input = QLineEdit()
        self.cost_price_input.setPlaceholderText("Enter cost price:")

        #add this widget to the second layout
        layout2.addWidget(self.cost_price_input)
        #create the inputbox to accept the cost price
        self.selling_price_input = QLineEdit()
        self.selling_price_input.setPlaceholderText("Enter selling price:")
        #add this widget to the second layout
        layout2.addWidget(self.selling_price_input)
        #create the inputbox to accept the cost price
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Enter quantity sold:")
        #add this widget to the second layout
        layout2.addWidget(self.quantity_input)

        #create the fifth layout
        layout3 = QHBoxLayout()
        #create the inputbox to accept the cost price
        cmdbtn = QPushButton("Compute Maize profit")
        cmdbtn.setFixedWidth(160)
        cmdbtn.clicked.connect(self.maize_profit)
        
        #create a reset button
        #create the inputbox to accept the cost price
        resetbtn = QPushButton("Reset App Data")
        resetbtn.setFixedWidth(160)
        resetbtn.clicked.connect(self.reset_app_data)
        layout3.addWidget(cmdbtn)
        layout3.addWidget(resetbtn)
        
        

        #create a form group
        form_one = QGroupBox("Maize")
        form_one.setFixedHeight(200)
        form_one.setStyleSheet("""
                                 QGroupBox{
                                     background-color:lightyellow;
                                 }
                                 """)
        form_layout = QVBoxLayout()
        form_layout.addLayout(layout1)
        form_layout.addLayout(layout2)
        form_layout.addLayout(layout3)
        form_one.setLayout(form_layout)


        #create the first layout, all these are for maize
        layout7 = QHBoxLayout()
        #create three inputbox to display information
        self.beans_profit_input = QLineEdit()
        self.beans_profit_input.setPlaceholderText("Profit here:")
        self.beans_profit_input.setReadOnly(True)

        self.beans_percent_profit_input = QLineEdit()
        self.beans_percent_profit_input.setPlaceholderText("Percent Profit here:")
        self.beans_percent_profit_input.setReadOnly(True)

        self.beans_total_cost_price = QLineEdit()
        self.beans_total_cost_price.setPlaceholderText("Total Cost price here:")
        self.beans_total_cost_price.setReadOnly(True)

        self.beans_total_selling_price = QLineEdit()
        self.beans_total_selling_price.setPlaceholderText("Total selling price here:")
        self.beans_total_selling_price.setReadOnly(True)

        #add all these widgets to the QHLayout
        layout7.addWidget(self.beans_profit_input)
        layout7.addWidget(self.beans_percent_profit_input)
        layout7.addWidget(self.beans_total_cost_price)
        layout7.addWidget(self.beans_total_selling_price)

        #create the second layouts
        layout8 = QHBoxLayout()
        #create the inputbox to accept the cost price
        self.beans_cost_price_input = QLineEdit()
        self.beans_cost_price_input.setPlaceholderText("Enter cost price:")
        #add this widget to the second layout
        layout8.addWidget(self.beans_cost_price_input)
        #create the inputbox to accept the cost price
        self.beans_seliing_price_input = QLineEdit()
        self.beans_seliing_price_input.setPlaceholderText("Enter selling price:")
        #add this widget to the second layout
        layout8.addWidget(self.beans_seliing_price_input)
        #create the inputbox to accept the cost price
        self.beans_quantity_input = QLineEdit()
        self.beans_quantity_input.setPlaceholderText("Enter quantity sold:")
        #add this widget to the second layout
        layout8.addWidget(self.beans_quantity_input)

        #create the fifth layout
        layout9 = QHBoxLayout()
        #create the inputbox to accept the cost price
        beans_cmdbtn = QPushButton("Compute Beans profit")
        beans_cmdbtn.setFixedWidth(160)
        beans_cmdbtn.clicked.connect(self.beans_profit)
        #add this widget to the second layout
        layout9.addWidget(beans_cmdbtn)

        #create a form group
        form_two = QGroupBox("Beans")
        form_two.setFixedHeight(200)
        form_two.setStyleSheet("""
                                 QGroupBox{
                                     background-color:lightblue;
                                 }
                                 """)
        form_layout1 = QVBoxLayout()
        form_layout1.addLayout(layout7)
        form_layout1.addLayout(layout8)
        form_layout1.addLayout(layout9)
        form_two.setLayout(form_layout1)


        #create the first layout, all these are for maize
        layout13 = QHBoxLayout()
        #create three inputbox to display information
        self.millet_profit_input = QLineEdit()
        self.millet_profit_input.setPlaceholderText("Profit here:")
        self.millet_profit_input.setReadOnly(True)

        self.millet_percent_profit_input = QLineEdit()
        self.millet_percent_profit_input.setPlaceholderText("Percent Profit here:")
        self.millet_percent_profit_input.setReadOnly(True)

        self.millet_total_cost_price = QLineEdit()
        self.millet_total_cost_price.setPlaceholderText("Total Cost price here:")
        self.millet_total_cost_price.setReadOnly(True)

        self.millet_total_selling_price = QLineEdit()
        self.millet_total_selling_price.setPlaceholderText("Total selling price here:")
        self.millet_total_selling_price.setReadOnly(True)

        #add all these widgets to the QHLayout
        layout13.addWidget(self.millet_profit_input)
        layout13.addWidget(self.millet_percent_profit_input)
        layout13.addWidget(self.millet_total_cost_price)
        layout13.addWidget(self.millet_total_selling_price)

        #create the second layouts
        layout14 = QHBoxLayout()
        #create the inputbox to accept the cost price
        self.millet_cost_price_input = QLineEdit()
        self.millet_cost_price_input.setPlaceholderText("Enter cost price:")
        #add this widget to the second layout
        layout14.addWidget(self.millet_cost_price_input)
        #create the inputbox to accept the cost price
        self.millet_seliing_price_input = QLineEdit()
        self.millet_seliing_price_input.setPlaceholderText("Enter selling price:")
        #add this widget to the second layout
        layout14.addWidget(self.millet_seliing_price_input)

        #create the inputbox to accept the cost price
        self.millet_quantity_input = QLineEdit()
        self.millet_quantity_input.setPlaceholderText("Enter quantity sold:")
        #add this widget to the second layout
        layout14.addWidget(self.millet_quantity_input)

        #create the fifth layout
        layout15 = QHBoxLayout()
        #create the inputbox to accept the cost price
        millet_cmdbtn = QPushButton("Compute Millet profit")
        millet_cmdbtn.setFixedWidth(160)
        millet_cmdbtn.clicked.connect(self.millet_profit)
        #add this widget to the second layout
        layout15.addWidget(millet_cmdbtn)
        

        #display all these layouts to the maize layout
        #create a form group
        form_three = QGroupBox("Millet")
        form_three.setFixedHeight(200)
        form_three.setStyleSheet("""
                                 QGroupBox{
                                     background-color:lightgreen;
                                 }
                                 """)
        form_layout2 = QVBoxLayout()
        form_layout2.addLayout(layout13)
        form_layout2.addLayout(layout14)
        form_layout2.addLayout(layout15)
        form_three.setLayout(form_layout2)

        
        #display the three form layouts as widgets on the general window
        general_layout = QVBoxLayout()
        general_layout.addWidget(form_one)
        general_layout.addWidget(form_two)
        general_layout.addWidget(form_three)
        self.setLayout(general_layout)

    def reset_app_data(self):
        #clear the maize data
        self.cost_price_input.setText(str(""))
        self.selling_price_input.setText(str(""))
        self.quantity_input.setText(str(""))
        self.total_selling_price.setText(str(""))
        self.profit_input.setText(str(""))
        self.total_cost_price.setText(str(""))
        self.percent_profit_input.setText(str(""))
        
        #implement beans data clear
        self.beans_cost_price_input.setText(str(""))
        self.beans_seliing_price_input.setText(str(""))
        self.beans_quantity_input.setText(str(""))
        self.beans_total_selling_price.setText(str(""))
        self.beans_profit_input.setText(str(""))
        self.beans_total_cost_price.setText(str(""))
        self.beans_percent_profit_input.setText(str(""))
        
        #implement millet data clear
        self.millet_cost_price_input.setText(str(""))
        self.millet_seliing_price_input.setText(str(""))
        self.millet_quantity_input.setText(str(""))
        self.millet_total_selling_price.setText(str(""))
        self.millet_profit_input.setText(str(""))
        self.millet_total_cost_price.setText(str(""))
        self.millet_percent_profit_input.setText(str(""))
        
    
    #define a function to handle the computations
    def maize_profit(self):
        print("The compute button has been clicked")
        try:
            #compute the maize profit
            #declare variable to hold values from inputboxes
            maize_cost_price = self.cost_price_input.text()
            maize_selling_price = self.selling_price_input.text()
            maize_quantity = self.quantity_input.text()
            mcp = float(maize_cost_price)
            msp = float(maize_selling_price)
            mq = float(maize_quantity)
            total_maize_cost = mcp*mq
            self.total_cost_price.setText(str("Total cost price: ")+str(total_maize_cost)+str(" USD"))

            total_maize_selling = msp*mq
            self.total_selling_price.setText(str("Total Selling price: ")+str(total_maize_selling)+str(" USD"))
            #profit
            maize_profit = msp-mcp
            self.profit_input.setText(str("Profit: ")+str(maize_profit)+str(" USD"))
            #percentage profit
            percentage_profit = (maize_profit/total_maize_cost)*100
            self.percent_profit_input.setText(str(" % Profit:")+str(percentage_profit)+str(" %"))
            
            #create a csv file from the user input
            record = {
                'cost_price':mcp,
                'selling_price':msp,
                'Total_cost_price':total_maize_cost,
                'Total_selling_price':total_maize_selling,
                'Profit':maize_profit,
                'Percent Profit':percentage_profit
            }
            maize_records.append(record)
            df = pd.DataFrame(maize_records)
            df.to_csv("Maize_records.csv",index=True)
            #display a message box
            QMessageBox.information(self,"Success Message.", "You successfully computed the Maize stock Data. And data stored to CSV")
        except ValueError:
            QMessageBox.warning(self,"Error Message.", "You must have all text boxes filled! and Text input is not allowed!")
            self.reset_app_data()
        
        except ZeroDivisionError:
            QMessageBox.warning(self,"Error Message.", "Division by zero not allowed, Ensure Total cost is a valid figure!")
            self.reset_app_data()
            
            
    def beans_profit(self):
        try:
            #compute the maize profit
            #declare variable to hold values from inputboxes
            beans_cost_price = self.beans_cost_price_input.text()
            beans_selling_price = self.beans_seliing_price_input.text()
            beans_quantity = self.beans_quantity_input.text()
            cp = float(beans_cost_price)
            sp = float(beans_selling_price)
            bq = float(beans_quantity)

            total_beans_cost = cp*bq
            self.beans_total_cost_price.setText(str("Total cost price: ")+str(total_beans_cost)+str(" USD"))

            total_beans_selling = sp*bq
            self.beans_total_selling_price.setText(str("Total selling price: ")+str(total_beans_selling)+str(" USD"))
            #profit
            beans_profit = total_beans_selling-total_beans_cost
            self.beans_profit_input.setText(str("Profit: ")+str(beans_profit)+str(" USD"))
            #percentage profit
            percentage_profit = (total_beans_cost/beans_profit)*100
            self.beans_percent_profit_input.setText(str("% Profit: ")+str(percentage_profit)+str(" %"))
            
            #create a csv file from the user input
            record = {
                'cost_price':cp,
                'selling_price':sp,
                'Total_cost_price':total_beans_cost,
                'Total_selling_price':total_beans_selling,
                'Profit':beans_profit,
                'Percent Profit':percentage_profit
            }
            beans_records.append(record)
            df = pd.DataFrame(beans_records)
            df.to_csv("Beans_records.csv",index=True)
            
            #display a message box
            QMessageBox.information(self,"Success Message.", "You successfully computed the Beans stock Data and CSV created.")
        
        except ValueError:
            QMessageBox.warning(self,"Error Message.", "You must have all text boxes filled! and Text input is not allowed!")
            self.reset_app_data()
        
        except ZeroDivisionError:
            QMessageBox.warning(self,"Error Message.", "Division by zero not allowed, ensure Total cost is a valid figure!")
            self.reset_app_data()

    def millet_profit(self):
        try:
            #compute the maize profit
            #declare variable to hold values from inputboxes
            cost_price = self.millet_cost_price_input.text()
            selling_price = self.millet_seliing_price_input.text()
            millet_quantity = self.millet_quantity_input.text()
            mcp = float(cost_price)
            msp = float(selling_price)
            mq = float(millet_quantity)
            
            total_millet_cost = mcp*mq
            self.millet_total_cost_price.setText(str("Total Cost Price: ")+str(total_millet_cost)+str(" USD"))

            total_millet_selling =msp*mq
            self.millet_total_selling_price.setText(str("Total selling price: ")+str(total_millet_selling)+str(" USD"))
            #profit
            millet_profit = total_millet_selling-total_millet_cost
            self.millet_profit_input.setText(str("Profit: ")+str(millet_profit)+str(" USD"))
            #percentage profit
            percentage_profit = (total_millet_cost/millet_profit)*100
            self.millet_percent_profit_input.setText(str("% Profit: ")+str(percentage_profit)+str("%"))
            
            #create a csv file from the user input
            record = {
                'cost_price':mcp,
                'selling_price':msp,
                'Total_cost_price':total_millet_cost,
                'Total_selling_price':total_millet_selling,
                'Profit':millet_profit,
                'Percent Profit':percentage_profit
            }
            millet_records.append(record)
            df = pd.DataFrame(millet_records)
            df.to_csv("Millet_records.csv",index=True)
            
            #display a message box
            QMessageBox.information(self,"Success Message.", "You successfully computed the Millet stock Data and CSV created.")
        
        except ValueError:
            QMessageBox.warning(self,"Error Message.", "You must have all text boxes filled! and Text input is not allowed!")
            self.reset_app_data()
        
        except ZeroDivisionError:
            QMessageBox.warning(self,"Error Message.", "Division by zero not allowed, ensure Total cost is a valid figure!")
            self.reset_app_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())