##### SIMPLE_JWT TOKEN 
##### language
1. [indonesia]
2. [english]

<br/>

1. ACCESS_TOKEN_LIFETIME: Specifies the duration until the access token will expire after being issued. You can set the expiration time in the form of a timedelta, for example, timedelta(seconds=3600) for one hour.
<br/>
2. SLIDING_TOKEN_REFRESH_LIFETIME: Specifies the duration until the refresh token will expire after being issued. The refresh token is used to extend the validity of the access token. If not set, it will use the same time as ACCESS_TOKEN_LIFETIME.
<br/>

3. SLIDING_TOKEN_REFRESH_LIFETIME_GRACE_PERIOD: Specifies the grace period before the refresh token expires. This means the refresh token can be used within a specific time before it actually expires. If not set, the refresh token can be used at any time before expiration.
<br/>

4. ROTATE_REFRESH_TOKENS: If set to True, every time the access token is refreshed, the refresh token will also be refreshed, and the old refresh token will become invalid. The default is False.
<br/>

5. ALGORITHM: Specifies the algorithm used to sign the JWT. The default is 'HS256', which uses HMAC-SHA-256. You can also use other algorithms like 'RS256' to use RSA-SHA-256.
<br/>

6. AUTH_HEADER_TYPES: Specifies the types of headers used to send the access token in requests. The default is ('Bearer',), which means the access token should be included in the Authorization header in the format 'Bearer <token>'.
<br/>

7. AUTH_TOKEN_CLASSES: Allows you to replace the classes for the access token and refresh token used. The default is to use the classes provided by djangorestframework-simplejwt.

















  [indonesia]: <./README.md>
  [english]: <./README-ENG.md>