from DoAn_LTV2 import app
from DoAn_LTV2.Xu_ly.Xu_ly import *
from flask import render_template, request,session



@app.route('/tuy-chon',methods=['GET','POST'])
def tuy_chon():
    danh_sach_cau_hoi = doc_database()
    de_thi = tao_de_thi(danh_sach_cau_hoi)
    session['De_thi'] = de_thi
   
    return render_template('MH_Tuy_chon.html', de_thi = session['De_thi'])

@app.route('/lam-tuy-chon', methods=['GET','POST'])
def lam_tuy_chon():
    chuoi_thong_bao = ''
    id_1 = ''
    bai_lam = []
    if session.get('Bai_lam'):
        bai_lam = session['Bai_lam']
    else:
        session['Bai_lam'] = []
        
    if request.method == "POST":
        tra_loi = {}
        id_1 = int(request.form.get('ID'))
        cau_hoi = tim_cau_hoi(id_1, session['De_thi'])
        # print(type(cau_hoi))
        # print(type(session['De_thi']))

        danh_sach_dap_an = cau_hoi['Danh_sach_dap_an']['Danh_sach_Chon_lua']
        # print(danh_sach_dap_an)
        a = request.form.get('dap_an_1')
        b = request.form.get('dap_an_2')
        tra_loi = {'STT':cau_hoi['ID'],'a':a,'b':b, 'Ten':cau_hoi['Ten']} 
        if a == None:
            a= ""
        if b == None:
            b= ""

        if len(danh_sach_dap_an) == 2:
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an']:
                chuoi_thong_bao = "Chính xác!"
            else:
                chuoi_thong_bao = "Không chính xác"
        elif len(danh_sach_dap_an) == 3:
            c = request.form.get('dap_an_3')
            tra_loi['c'] = c
            if c == None:
                c = ''
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an'] and c == danh_sach_dap_an[2]['La_dap_an']:
                chuoi_thong_bao = "Chính xác"
            else:
                chuoi_thong_bao = "Không chính xác"
        elif len(danh_sach_dap_an) == 4:
            c = request.form.get('dap_an_3')
            d = request.form.get('dap_an_4')
            tra_loi['c'] = c
            tra_loi['d'] = d
            if c == None:
                c=''
            if d == None:
                d=''
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an'] and c == danh_sach_dap_an[2]['La_dap_an'] and d == danh_sach_dap_an[3]['La_dap_an']:
                chuoi_thong_bao = "Chính xác"
            else:
                chuoi_thong_bao = "Không chính xác"
        
        tra_loi['Danh_sach_dap_an'] = danh_sach_dap_an
        tra_loi['Ket_qua'] = chuoi_thong_bao
        bai_lam.append(tra_loi)
        session['De_thi'].remove(cau_hoi)
        session['Bai_lam'] = bai_lam
        
    return render_template('MH_Lam_tuy_chon.html', Chuoi_thong_bao = chuoi_thong_bao, id = id_1)