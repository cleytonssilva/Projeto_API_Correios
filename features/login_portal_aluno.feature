# language: pt

Funcionalidade: Login no Portal do Aluno
  Como aluno cadastrado
  Quero autenticar-me no Portal do Aluno
  Para acessar os recursos disponíveis na minha área acadêmica

  Cenário: Login realizado com credenciais válidas
    Dado que o aluno está na página de login do Portal do Aluno
    E possui usuário e senha válidos
    Quando informar o usuário no campo de login
    E informar a senha no campo de senha
    E clicar no botão "Entrar"
    Então o sistema deve autenticar o aluno com sucesso
    E deve direcioná-lo para a página inicial do Portal do Aluno
