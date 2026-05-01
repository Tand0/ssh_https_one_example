FROM nginx:latest

# 環境変数の設定 (Pythonのpycファイルを作成しない、ログをバッファリングしない)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN rm -rf /etc/nginx/sites-enabled/default
RUN rm -rf /etc/nginx/sites-available/default
RUN mkdir -p /etc/ssl/certs
COPY ./ssh/server.crt /etc/ssl/certs
RUN mkdir -p /etc/ssl/private
COPY ./ssh/server.key /etc/ssl/private

# 作業ディレクトリの設定
WORKDIR /etc/nginx/conf.d
COPY reverse_proxy.conf .

# 起動ポートの指定
EXPOSE 8082
