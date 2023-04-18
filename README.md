Проеĸт автотестов api.regress
===========

<!-- Технологии -->
### Технологии используемые в проеĸте


<p  align="center">
  <code><img width="5%" title="Pycharm" src="./attachments/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="./attachments/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="./attachments/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="./attachments/logo/selene.png"></code>
  <code><img width="5%" title="GitHub" src="./attachments/logo/github.png"></code>
  <code><img width="5%" title="Allure Report" src="./attachments/logo/allure_report.png"></code>
  <code><img width="5%" title="Jenkins" src="./attachments/logo/jenkins.png"></code>
  <code><img width="5%" title="Requests" src="./attachments/logo/requests.png"></code>
  <code><img width="10%" title="Requests" src="./attachments/logo/Instrument-Allure-TestOps.png"></code>
</p>

### Что выполняет тест:

- Создание нового пользователя по средствам api
- Получения информации о пользователе по средствам api
- Обновление информации о пользователе по средствам api

![This is an image](attachments/screenshots/test.png)


## Запуск тестов из терминала
```bash
pytest tests/regress_in --env=prod
```

В проекте используется logger
![This is an image](attachments/screenshots/logger.png)

<!-- Jenkins -->

### Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/Api_tests_Vishnyakova/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение
![This is an image](attachments/screenshots/jenkins.png)

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="attachments/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты автоматически сохраняются. Чтобы посмотреть Allure отчет нужно нажать на иконке allure report у сборки.
![This is an image](attachments/screenshots/allure.png)

<!-- Allure TestOps -->

### <img width="8%" title="Allure TestOps" src="attachments/logo/Instrument-Allure-TestOps.png"> Allure report

##### После прохождения тестов, Создается ланч в Allure TestOps c результатом прогона тестов. Что бы просмотреть ланч нужно нажать на иконку allure testops у сборки.
![This is an image](attachments/screenshots/allure_testops.png)

 
