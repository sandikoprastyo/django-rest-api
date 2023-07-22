##### SIMPLE_JWT TOKEN 
##### language
1. [indonesia]
2. [english]

<br/>

1. ACCESS_TOKEN_LIFETIME: Menyatakan berapa lama token akses (access token) akan kedaluwarsa setelah dikeluarkan. Anda dapat mengatur waktu kedaluwarsa dalam bentuk timedelta, misalnya timedelta(seconds=3600) untuk satu jam.
<br/>
2. SLIDING_TOKEN_REFRESH_LIFETIME: Menyatakan berapa lama token refresh (refresh token) akan kedaluwarsa setelah dikeluarkan. Refresh token digunakan untuk memperpanjang masa aktif token akses. Jika tidak diatur, maka akan menggunakan waktu yang sama dengan ACCESS_TOKEN_LIFETIME.
<br/>

3. SLIDING_TOKEN_REFRESH_LIFETIME_GRACE_PERIOD: Menyatakan waktu toleransi sebelum token refresh kedaluwarsa. Artinya, token refresh dapat digunakan dalam waktu tertentu sebelum token tersebut benar-benar kedaluwarsa. Jika tidak diatur, maka token refresh dapat digunakan kapan saja sebelum kedaluwarsa.
<br/>

4. ROTATE_REFRESH_TOKENS: Jika diatur sebagai True, setiap kali token akses diperbarui (refreshed), token refresh akan diperbarui juga dan token refresh lama akan dibuat tidak berlaku lagi. Default-nya adalah False.
<br/>

5. ALGORITHM: Menyatakan algoritma yang digunakan untuk menandatangani token JWT. Default-nya adalah 'HS256', yang menggunakan HMAC-SHA-256. Anda juga dapat menggunakan algoritma lain seperti 'RS256' untuk menggunakan RSA-SHA-256.
<br/>

6. AUTH_HEADER_TYPES: Menyatakan jenis header yang digunakan untuk mengirimkan token akses dalam permintaan. Default-nya adalah ('Bearer',), yang berarti token akses harus dimasukkan dalam header Authorization dalam format 'Bearer <token>'.
<br/>

7. AUTH_TOKEN_CLASSES: Mengizinkan Anda mengganti kelas token akses dan token refresh yang digunakan. Default-nya adalah menggunakan kelas yang disediakan oleh djangorestframework-simplejwt.

















  [indonesia]: <./README.md>
  [english]: <./README-ENG.md>