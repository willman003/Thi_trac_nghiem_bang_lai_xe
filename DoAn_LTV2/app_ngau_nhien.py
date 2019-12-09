from DoAn_LTV2 import app
from DoAn_LTV2.Xu_ly.Xu_ly import *
from flask import render_template, request, session,redirect, url_for

import random


@app.route('/ngau-nhien',methods=['GET','POST'])
def ngau_nhien():
    if session.get('Mo_dau'):
        mo_dau = session['Mo_dau']
    else:
        mo_dau = ''    
    if request.form.get('Mo_Dau'):
        mo_dau = request.form.get('Mo_Dau')
        session['Mo_dau'] = mo_dau
    chuoi_thong_bao = ''



    if session.get('Danh_sach_ID'):
        danh_sach_ngau_nhien = session.get('Danh_sach_ID')
    else:
        danh_sach_ngau_nhien = []

    danh_sach_cau_hoi = doc_database()
    if request.form.get('DiChuyen') == 'Chính xác' or len(danh_sach_ngau_nhien)== 0:
        id_ngau_nhien = random.randint(danh_sach_cau_hoi[0]['ID'],len(danh_sach_cau_hoi)+1)
        while id_ngau_nhien in danh_sach_ngau_nhien:
            id_ngau_nhien = random.ranint(danh_sach_cau_hoi[0]['ID'],len(danh_sach_cau_hoi)+1)
        danh_sach_ngau_nhien.append(id_ngau_nhien)
        session['Danh_sach_ID'] = danh_sach_ngau_nhien
       
    else:
        id_ngau_nhien = session['ID']
    cau_hoi = tim_cau_hoi(id_ngau_nhien, danh_sach_cau_hoi)
    if request.form.get('DiChuyen') != "Chính xác":
        session['ID'] = danh_sach_ngau_nhien[-1]
    else:
        session['ID'] = cau_hoi['ID']

    
    if request.form.get('dieu_khien') == '1':
        
        danh_sach_dap_an = cau_hoi['Danh_sach_dap_an']['Danh_sach_Chon_lua']
        
        a = request.form.get('dap_an_1')
        b = request.form.get('dap_an_2')
        danh_sach_dap_an[0]['Lua_chon'] = a
        danh_sach_dap_an[1]['Lua_chon'] = b
        if a == None:
            a = ""
        if b == None:
            b = ""

        if len(danh_sach_dap_an) == 2:
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an']:
                chuoi_thong_bao = "Chính xác"
            else:
                chuoi_thong_bao = "Không chính xác"
        elif len(danh_sach_dap_an) == 3:
            c = request.form.get('dap_an_3')
            danh_sach_dap_an[2]['Lua_chon'] = c
            if c == None:
                c = ''
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an'] and c == \
                    danh_sach_dap_an[2]['La_dap_an']:
                chuoi_thong_bao = "Chính xác"
            else:
                chuoi_thong_bao = "Không chính xác"
        elif len(danh_sach_dap_an) == 4:
            c = request.form.get('dap_an_3')
            d = request.form.get('dap_an_4')
            danh_sach_dap_an[2]['Lua_chon'] = c
            danh_sach_dap_an[3]['Lua_chon'] = d
            if c == None:
                c = ''
            if d == None:
                d = ''
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an'] and c == \
                    danh_sach_dap_an[2]['La_dap_an'] and d == danh_sach_dap_an[3]['La_dap_an']:
                chuoi_thong_bao = "Chính xác"
            else:
                chuoi_thong_bao = "Không chính xác"
        print(danh_sach_dap_an)


    return render_template("/MH_Ngau_nhien.html",mo_dau = mo_dau, cau_hoi = cau_hoi, chuoi_thong_bao = chuoi_thong_bao, id =session['ID'])

