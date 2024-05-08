FROM mysql

ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=webapp

CMD ["--default-authentication-plugin=mysql_native_password"]