from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTesteCase(APITestCase):
    """ Classe para realizar testes para o Cursos."""
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        # Em vez de utilizar os cursos que estiverem no BD, serão criados novos cursos para os testes.
        self.curso_1 = Curso.objects.create(
            codigo_curso = 'CTT1', 
            descricao = 'Curso teste 1',
            nivel = 'B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso = 'CTT2', 
            descricao = 'Curso teste 2',
            nivel = 'A'
        )

    # def test_falhador(self)    :
    #     self.fail('Teste falhou intencionalmente.')

    def test_requisicao_get_para_listar_cursos(self):
        """ Teste para verificar a requisicao GET que lista os cursos."""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_incluir_curso(self):
        """ Teste para verificar a requisicao POST para incluir um curso."""
        dados = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso teste 3',
            'nivel': 'B'
        }
        response = self.client.post(self.list_url, data=dados)

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
    def test_requisicao_delete_para_remover_curso(self):
        """ Teste para verificar que a requisicao DELETE para o curso NAO será permitida. """
        response = self.client.delete('/cursos/1/')
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_nivel_curso(self):
        """ Teste para verificar a requisicao PUT para atualizar um nível de um curso. """    
        dados = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso teste 1 atualizado',
            'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data=dados)
        self.assertEquals(response.status_code, status.HTTP_200_OK)