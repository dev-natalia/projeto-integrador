def test_criar_ceu_sem_auth(client):
    response = client.post(
        "/ceu",
        json={
            "nome": "CEU Test",
            "bairro": "Bairro Test",
            "endereco": "End Test",
            "telefone": "(11) 99999-0020",
        },
    )
    assert response.status_code == 401


def test_criar_ceu_com_auth(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.post(
        "/ceu",
        json={
            "nome": "CEU Test",
            "bairro": "Bairro Test",
            "endereco": "End Test",
            "telefone": "(11) 99999-0020",
        },
        headers=headers,
    )
    assert response.status_code == 201
    assert response.json()["nome"] == "CEU Test"


def test_listar_ceus(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    client.post(
        "/ceu",
        json={
            "nome": "CEU 1",
            "bairro": "Bairro 1",
            "endereco": "End 1",
            "telefone": "(11) 99999-0021",
        },
        headers=headers,
    )
    client.post(
        "/ceu",
        json={
            "nome": "CEU 2",
            "bairro": "Bairro 2",
            "endereco": "End 2",
            "telefone": "(11) 99999-0022",
        },
        headers=headers,
    )

    response = client.get("/ceu")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2


def test_atualizar_ceu(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    post_res = client.post(
        "/ceu",
        json={
            "nome": "CEU Old",
            "bairro": "Bairro Old",
            "endereco": "End Old",
            "telefone": "(11) 99999-0023",
        },
        headers=headers,
    )
    ceu_id = post_res.json()["id"]

    put_res = client.put(
        f"/ceu/{ceu_id}",
        json={
            "nome": "CEU New",
            "bairro": "Bairro New",
            "endereco": "End New",
            "telefone": "(11) 99999-0024",
        },
        headers=headers,
    )
    assert put_res.status_code == 200
    assert put_res.json()["nome"] == "CEU New"


def test_deletar_ceu(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    post_res = client.post(
        "/ceu",
        json={
            "nome": "CEU to Delete",
            "bairro": "B",
            "endereco": "E",
            "telefone": "(11) 99999-0025",
        },
        headers=headers,
    )
    ceu_id = post_res.json()["id"]

    del_res = client.delete(f"/ceu/{ceu_id}", headers=headers)
    assert del_res.status_code == 200
    assert del_res.json() is True

    get_res = client.get("/ceu")
    assert not any(ceu["id"] == ceu_id for ceu in get_res.json())
