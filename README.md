# Todo App

## Proje Açıklaması

1.Kullanıcı kayıt ekranından kayıt olup, sisteme giriş yapabilecekler.

2.Oturum açan kullanıcılar, kendisine ait kayıtlı olan yapılacaklar listesini görebilecektir.

3.Oturum açmış kullanıcılar kendilerine ait yeni görevler ekleyebilecek. Eklemiş oldukları bu görevleri hem güncelleyebilecekler hem de silebilecekler.


## Projede kullanılan teknolojiler

- Python
- Django
- sqlite3

## Kurulum

1. Bu projeyi yerel makinenize klonlayın:

   ```shell
   git clone https://github.com/Ahmetkcak/todo-app.git
2. Proje dizinine gidin:
    ```shell
   cd todo_app
3. Veritabanını oluşturun:
    ```shell
    python manage.py migrate
    python manage.py makemigrations
4. Sunucuyu çalıştırın:
    ```
    python manage.py runserver
5. Tarayıcınızda aşağıdaki URL'yi açın:
    ```
    http://127.0.0.1:8000/
## Projede kullanılan kullanıcılar 

1. Admin kullanıcı için :
    
    username = ahmet , password = 12345

2. Default kullanıcı için :

     username = user , password = tester12345