import pytest

@pytest.fixture
def ceu_id(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.post("/ceu", json={"nome": "CEU Test Ativ", "bairro": "B", "endereco": "E"}, headers=headers)
    return response.json()["id"]

def test_criar_atividade(client, admin_token, ceu_id):
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {
        "titulo": "Atividade de Yoga",
        "descricao": "Yoga matinal",
        "data": "2023-01-01",
        "ceu_id": ceu_id
    }
    response = client.post("/atividades", json=data, headers=headers)
    assert response.status_code == 201
    assert response.json()["titulo"] == "Atividade de Yoga"

def test_listar_atividades_com_filtros(client, admin_token, ceu_id):
    headers = {"Authorization": f"Bearer {admin_token}"}
    
    client.post("/atividades", json={
        "titulo": "Atividade 1", "descricao": "D1", "data": "2023-05-01", "ceu_id": ceu_id
    }, headers=headers)
    
    ceu2_res = client.post("/ceu", json={"nome": "CEU 2", "bairro": "B", "endereco": "E"}, headers=headers)
    ceu2_id = ceu2_res.json()["id"]
    client.post("/atividades", json={
        "titulo": "Atividade 2", "descricao": "D2", "data": "2023-06-01", "ceu_id": ceu2_id
    }, headers=headers)

    res_ceu1 = client.get(f"/atividades?ceu_id={ceu_id}")
    assert len(res_ceu1.json()) == 1
    assert res_ceu1.json()[0]["titulo"] == "Atividade 1"

    res_data = client.get("/atividades?data_filtro=2023-05-01")
    assert len(res_data.json()) == 1
    assert res_data.json()[0]["titulo"] == "Atividade 1"
    
def test_atualizar_atividade(client, admin_token, ceu_id):
    headers = {"Authorization": f"Bearer {admin_token}"}
    post_res = client.post("/atividades", json={
        "titulo": "Atividade Old", "descricao": "D1", "data": "2023-01-01", "ceu_id": ceu_id
    }, headers=headers)
    ativ_id = post_res.json()["id"]

    put_res = client.put(f"/atividades/{ativ_id}", json={
        "titulo": "Atividade New", "descricao": "D2", "data": "2023-01-01", "ceu_id": ceu_id
    }, headers=headers)
    assert put_res.status_code == 200
    assert put_res.json()["titulo"] == "Atividade New"

def test_deletar_atividade(client, admin_token, ceu_id):
    headers = {"Authorization": f"Bearer {admin_token}"}
    post_res = client.post("/atividades", json={
        "titulo": "Atividade to del", "descricao": "D1", "data": "2023-01-01", "ceu_id": ceu_id
    }, headers=headers)
    ativ_id = post_res.json()["id"]

    del_res = client.delete(f"/atividades/{ativ_id}", headers=headers)
    assert del_res.status_code == 200
    assert del_res.json() is True
