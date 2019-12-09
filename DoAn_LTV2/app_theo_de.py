from DoAn_LTV2 import app
from DoAn_LTV2.Xu_ly.Xu_ly import *
from flask import render_template, request, session,redirect, url_for

@app.route('/theo-de',methods=['GET','POST'])
def theo_de():
    bo_de_thi = []
    cau_hoi = {}
    ma_de_thi = ''
    danh_sach_cau_hoi = doc_database()
    
    for i in range(1,9):
        de_thi = {}
        de_thi['Ma_de_thi'] = str(i)
        de_thi['Noi_dung'] = tao_de_thi(danh_sach_cau_hoi)
        bo_de_thi.append(de_thi)
    de_thi = ''
    if request.form.get('TH'):
        ma_de_thi = request.form.get('TH')
        session['Ma_de_thi'] = ma_de_thi
        # print(ma_de_thi)
        for item in bo_de_thi:
            if item['Ma_de_thi'] == ma_de_thi:
                de_thi = item['Noi_dung']
                # print(len(de_thi))
               
        i = 1
        for cau_hoi in de_thi:
            cau_hoi['STT'] = str(i)
            # print(cau_hoi['STT'])
            i+=1
        cau_hoi = de_thi[0]
    session['De_thi'] = de_thi
    # print(de_thi[19])
    session['STT'] = 0
    session['Bai_lam'] = []
    
       
    return render_template("/MH_Theo_de.html",bo_de_thi = bo_de_thi, de_thi = de_thi, cau_hoi = cau_hoi, ma_de_thi = ma_de_thi)

@app.route('/de-thi', methods= ['GET','POST'])
def lam_de():
        
    cau_hoi = session['De_thi'][session['STT']]
    
    tra_loi = {}
    if request.method == 'POST':
        a= request.form.get('dap_an_1')
        b= request.form.get('dap_an_2')
        tra_loi = {'STT':cau_hoi['STT'],'a':a,'b':b}
        
        danh_sach_dap_an = cau_hoi['Danh_sach_dap_an']['Danh_sach_Chon_lua']
        if len(danh_sach_dap_an) == 3:
            c = request.form.get('dap_an_3')
            tra_loi['c'] = c
            
        if len(danh_sach_dap_an) == 4:
            c = request.form.get('dap_an_3')
            d = request.form.get('dap_an_4')
            tra_loi['c'] = c
            tra_loi['d'] = d
        tra_loi['Danh_sach_dap_an'] = danh_sach_dap_an
        
        session['Bai_lam'].append(tra_loi)
        session['STT'] += 1
        if session['STT'] <= 19:
            
            cau_hoi = session['De_thi'][session['STT']]
    # print(session['Bai_lam'])
       
   

    return render_template('MH_De_thi.html',cau_hoi = cau_hoi)

@app.route('/nop-bai',methods = ['GET','POST'])
def nop_bai():
    bai_lam = session['Bai_lam']
    chuoi_thong_bao = ''
    so_cau_dung = 0

    for cau_tra_loi in bai_lam:
        
        danh_sach_dap_an = cau_tra_loi['Danh_sach_dap_an']
        a = cau_tra_loi['a']
        b = cau_tra_loi['b']
        if a == None:
            a= ""
        if b == None:
            b= ""

        if len(danh_sach_dap_an) == 2:
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an']:
                chuoi_thong_bao = "Chính xác"
            else:
                chuoi_thong_bao = "Không chính xác"
        elif len(danh_sach_dap_an) == 3:
            c = cau_tra_loi['c']
            if c == None:
                c = ''
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an'] and c == danh_sach_dap_an[2]['La_dap_an']:
                chuoi_thong_bao = "Chính xác"
            else:
                chuoi_thong_bao = "Không chính xác"
        elif len(danh_sach_dap_an) == 4:
            c = cau_tra_loi['c']
            d = cau_tra_loi['d']
            if c == None:
                c=''
            if d == None:
                d=''
            if a == danh_sach_dap_an[0]['La_dap_an'] and b == danh_sach_dap_an[1]['La_dap_an'] and c == danh_sach_dap_an[2]['La_dap_an'] and d == danh_sach_dap_an[3]['La_dap_an']:
                chuoi_thong_bao = "Chính xác"
            else:
                chuoi_thong_bao = "Không chính xác"
        cau_tra_loi['Ket_qua'] = chuoi_thong_bao
        
        
        if cau_tra_loi['Ket_qua'] == "Chính xác":
            so_cau_dung += 1
        # if cau_tra_loi['STT'] == "16":
        #     print(type(d))
        #     if a == danh_sach_dap_an[3]['La_dap_an']:
        #         print('True')
        #     print(cau_tra_loi['Danh_sach_dap_an'])
    # print(session['De_thi'])

    return render_template('MH_Nop_bai.html', bai_lam = bai_lam, chuoi_thong_bao=chuoi_thong_bao, so_cau_dung = so_cau_dung )

@app.route('/log-out',methods=['GET'])
def log_out():
    session.clear()
    return redirect(url_for('index'))
