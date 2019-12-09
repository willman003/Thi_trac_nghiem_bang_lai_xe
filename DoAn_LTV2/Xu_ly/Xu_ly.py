duong_dan = "DoAn_LTV2/Du_lieu/trac_nghiem_thi_ly_thuyet_a1.db"
import sqlite3
import ast
import random


def doc_database():
    danh_sach_cau_hoi = []
    cau_truy_van = "SELECT * from CHTN"
    conn = sqlite3.connect(duong_dan)
    cursor = conn.cursor()
    cursor.execute(cau_truy_van)
    for row in cursor:
        cau_hoi = {}
        cau_hoi['ID'] = row[0]
        cau_hoi['Anh'] = row[1]
        cau_hoi['Ten'] = row[2]
        cau_hoi['Noi_dung'] = row[3]
        cau_hoi['Co_hinh'] = row[4]
        cau_hoi['Danh_sach_dap_an'] = ast.literal_eval(row[5])
        danh_sach_cau_hoi.append(cau_hoi)
    return danh_sach_cau_hoi

def tim_cau_hoi(ID, danh_sach_cau_hoi):
    cau_hoi = {}
    for cau_hoi_nho in danh_sach_cau_hoi:
        if cau_hoi_nho['ID'] == ID:
            cau_hoi.update(cau_hoi_nho)
            break
    return cau_hoi

def tao_de_thi(danh_sach_cau_hoi):
    danh_sach_ngau_nhien = []
    danh_sach_ngau_nhien_1 = []
    danh_sach_ngau_nhien_2 = []
    de_thi = []
    bo_cau_hoi_luat = []
    bo_cau_hoi_bien_bao = []
    bo_cau_hoi_sa_hinh = []
    
    for cau_hoi in danh_sach_cau_hoi:
        noi_dung = cau_hoi['Noi_dung']
        co_hinh = cau_hoi['Co_hinh']
        chuoi_noi_dung = noi_dung.split()
        if co_hinh == "":
            bo_cau_hoi_luat.append(cau_hoi['ID'])
        else:
            for tu in chuoi_noi_dung:
                if co_hinh != "" and tu.lower() == "biển":
                    bo_cau_hoi_bien_bao.append(cau_hoi['ID'])
                    break
            else:
                bo_cau_hoi_sa_hinh.append(cau_hoi['ID'])
                    
   
    for i in range(10):
        id_ngau_nhien = random.randint(bo_cau_hoi_luat[0], bo_cau_hoi_luat[-1])
        while id_ngau_nhien in danh_sach_ngau_nhien:
            id_ngau_nhien = random.randint(bo_cau_hoi_luat[0], bo_cau_hoi_luat[-1])
        danh_sach_ngau_nhien.append(id_ngau_nhien)
        cau_hoi = tim_cau_hoi(id_ngau_nhien,danh_sach_cau_hoi)
        de_thi.append(cau_hoi)
    for i in range(5):
        id_ngau_nhien_1 = random.randint(bo_cau_hoi_bien_bao[0], bo_cau_hoi_bien_bao[-1])
               
        while id_ngau_nhien_1 in danh_sach_ngau_nhien_1:
            id_ngau_nhien_1 = random.randint(bo_cau_hoi_bien_bao[0], bo_cau_hoi_bien_bao[-1])
        danh_sach_ngau_nhien_1.append(id_ngau_nhien_1)
        cau_hoi_bien_bao = tim_cau_hoi(id_ngau_nhien_1, danh_sach_cau_hoi)
        de_thi.append(cau_hoi_bien_bao)
        
    for i in range(5):
        id_ngau_nhien_2 =  random.randint(bo_cau_hoi_sa_hinh[0], bo_cau_hoi_sa_hinh[-1])
        while id_ngau_nhien_2 in danh_sach_ngau_nhien_2:
            id_ngau_nhien_2 =  random.randint(bo_cau_hoi_sa_hinh[0], bo_cau_hoi_sa_hinh[-1])
        danh_sach_ngau_nhien_2.append(id_ngau_nhien_2)    
        cau_hoi_sa_hinh = tim_cau_hoi(id_ngau_nhien_2, danh_sach_cau_hoi)
        de_thi.append(cau_hoi_sa_hinh)
    
    return de_thi
