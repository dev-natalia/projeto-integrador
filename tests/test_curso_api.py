import pytest


@pytest.fixture
def ceu_id(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.post(
        "/ceu",
        json={
            "nome": "CEU Test Curso",
            "bairro": "B",
            "endereco": "E",
            "telefone": "(11) 99999-0010",
        },
        headers=headers,
    )
    return response.json()["id"]


def test_criar_curso(client, admin_token, ceu_id):
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {
        "titulo": "Curso de Python",
        "descricao": "Aprenda Python do zero",
        "data": "2023-01-01",
        "hora_inicio": "18:00:00",
        "ceu_id": ceu_id,
    }
    response = client.post("/cursos", json=data, headers=headers)
    assert response.status_code == 201
    assert response.json()["titulo"] == "Curso de Python"


def test_listar_cursos_com_filtros(client, admin_token, ceu_id):
    headers = {"Authorization": f"Bearer {admin_token}"}

    # Criar um curso no periodo
    client.post(
        "/cursos",
        json={
            "titulo": "Curso 1",
            "descricao": "D1",
            "data": "2023-05-01",
            "hora_inicio": "14:00:00",
            "ceu_id": ceu_id,
        },
        headers=headers,
    )

    # Criar outro curso em outro CEU e outro periodo
    ceu2_res = client.post(
        "/ceu",
        json={
            "nome": "CEU 2",
            "bairro": "B",
            "endereco": "E",
            "telefone": "(11) 99999-0011",
        },
        headers=headers,
    )
    ceu2_id = ceu2_res.json()["id"]
    client.post(
        "/cursos",
        json={
            "titulo": "Curso 2",
            "descricao": "D2",
            "data": "2023-06-01",
            "hora_inicio": "15:00:00",
            "ceu_id": ceu2_id,
        },
        headers=headers,
    )

    # Testar filtro por ceu_id
    res_ceu1 = client.get(f"/cursos?ceu_id={ceu_id}")
    assert len(res_ceu1.json()) == 1
    assert res_ceu1.json()[0]["titulo"] == "Curso 1"

    # Testar filtro por data igual à data do curso
    res_data = client.get("/cursos?data_filtro=2023-05-01")
    assert len(res_data.json()) == 1
    assert res_data.json()[0]["titulo"] == "Curso 1"

    # Testar filtro por data que nao existe
    res_data_empty = client.get("/cursos?data_filtro=2024-01-01")
    assert len(res_data_empty.json()) == 0


def test_atualizar_curso(client, admin_token, ceu_id):
    headers = {"Authorization": f"Bearer {admin_token}"}
    post_res = client.post(
        "/cursos",
        json={
            "titulo": "Curso Old",
            "descricao": "D1",
            "data": "2023-01-01",
            "hora_inicio": "08:00:00",
            "ceu_id": ceu_id,
        },
        headers=headers,
    )
    curso_id = post_res.json()["id"]

    put_res = client.put(
        f"/cursos/{curso_id}",
        json={
            "titulo": "Curso New",
            "descricao": "D2",
            "data": "2023-01-01",
            "hora_inicio": "09:00:00",
            "ceu_id": ceu_id,
        },
        headers=headers,
    )
    assert put_res.status_code == 200
    assert put_res.json()["titulo"] == "Curso New"


def test_deletar_curso(client, admin_token, ceu_id):
    headers = {"Authorization": f"Bearer {admin_token}"}
    post_res = client.post(
        "/cursos",
        json={
            "titulo": "Curso to del",
            "descricao": "D1",
            "data": "2023-01-01",
            "hora_inicio": "08:00:00",
            "ceu_id": ceu_id,
        },
        headers=headers,
    )
    curso_id = post_res.json()["id"]

    del_res = client.delete(f"/cursos/{curso_id}", headers=headers)
    assert del_res.status_code == 200
    assert del_res.json() is True
