from flask import Flask

app = Flask(__name__)
app.secret_key = '2266'

import DoAn_LTV2.app_index
import DoAn_LTV2.app_tuy_chon
import DoAn_LTV2.app_ngau_nhien
import DoAn_LTV2.app_theo_de