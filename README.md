Blasti REST API
Welcome to the Blasti REST API documentation. This API allows clients to access and manipulate data for the Blasti e-ticketing platform, enabling the purchase of tickets and access to exclusive merchandise for sporting events in Tunisia.

Endpoints:
The following endpoints are available for interacting with the Blasti API:

Store Categories
GET /store_cat: Retrieve a list of store categories.

Description: This endpoint returns a list of all store categories available on the Blasti platform. Each store category includes a unique ID and a name.
Success: 200 OK
Failure: 401 UNAUTHORIZED
POST /store_cat: Create a new store category.

Description: This endpoint allows an authenticated user to create a new store category on the Blasti platform. The request body should include the name of the store category.
Success: 201 CREATED
Failure: 400 BAD REQUEST, 401 UNAUTHORIZED
GET /store_cat/:storeCatId: Retrieve a specific store category.

Description: This endpoint returns detailed information about a specific store category, including its ID and name.
Success: 200 OK
Failure: 401 UNAUTHORIZED, 404 NOT FOUND
PUT /store_cats/:storeCatId: Update a specific store category.

Description: This endpoint allows an authenticated user to update the name of a specific store category on the Blasti platform. The request body should include the updated name.
Success: 200 OK
Failure: 400 BAD REQUEST, 401 UNAUTHORIZED, 404 NOT FOUND

Merchandise
GET /merchandise: Retrieve a list of merchandise.

Description: This endpoint returns a list of all merchandise available on the Blasti platform. Each piece of merchandise includes a unique ID, a name, a description, and a price.
Success: 200 OK
Failure: 401 UNAUTHORIZED
POST /merchandise: Create a new piece of merchandise.

Description: This endpoint allows an authenticated user to create a new piece of merchandise on the Blasti platform. The request body should include the name, description, and price of the merchandise.
Success: 201 CREATED
Failure: 400 BAD REQUEST, 401 UNAUTHORIZED
GET /merchandise/:merchandiseId: Retrieve a specific piece of merchandise.

Description: This endpoint returns detailed information about a specific piece of merchandise, including its ID, name, description, and price.
Success: 200 OK
Failure: 401 UNAUTHORIZED, 404 NOT FOUND
PUT /merchandise/:merchandiseId: Update a specific piece of merchandise.

Description: This endpoint allows an authenticated user to update the name, description, or price of a specific piece of merchandise on the Blasti platform. The request body should include the updated information.
Success: 200 OK
Failure: 400 BAD REQUEST, 401 UNAUTHORIZED, 404 NOT FOUND
DELETE /merchandise/:merchandiseId: Delete a specific piece of merchandise.

Description: This endpoint allows an authenticated user to delete a specific piece of merchandise from the Blasti platform.
Success: 200 OK
Failure: 401 UNAUTHORIZED, 404 NOT FOUND

Users
POST /users/register: Register a new user.

Description: This endpoint allows a new user to register for an account on the Blasti platform. The request body should include the user's email address and password.
Success: 201 CREATED
Failure: 400 BAD REQUEST
POST /users/login: Log in an existing user.

Description: This endpoint allows an existing user to log in to their account on the Blasti platform. The request body should include the user's email address and password. Upon successful login, a JSON web token will be returned.
Success: 200 OK
Failure: 400 BAD REQUEST, 401 UNAUTHORIZED
POST /users/logout: Log out the current user.

Description: This endpoint allows the current user to log out of their account on the Blasti platform.
Success: 200 OK
Failure: 401 UNAUTHORIZED
GET /users/me: Retrieve the current user's information.

Description: This endpoint returns detailed information about the current user, including their ID and email address.
Success: 200 OK
Failure: 401 UNAUTHORIZED
PUT /users/me: Update the current user's information.

Description: This endpoint allows the current user to update their email address or password. The request body should include the updated information.
Success: 200 OK
Failure: 400 BAD REQUEST, 401 UNAUTHORIZED
DELETE /users/me: Delete the current user's account.

Description: This endpoint allows the current user to delete their account from the Blasti platform.
Success: 200 OK
Failure: 401 UNAUTHORIZED



In order to securely authenticate users, the Blasti REST API uses JSON web tokens (JWTs). Upon successful login, a JWT is returned to the user and must be included in the header of subsequent requests to protected endpoints. The JWT is cryptographically signed and can be verified by the server to ensure that it was not tampered with. This allows the server to trust the authenticity of requests made by logged-in users and provide them with access to protected resources. The use of JWTs helps to prevent unauthorized access to the Blasti platform and ensure the security of user data.