# crawling

## 차세대 분산 시스템 텀 프로젝트


* slave
* master


## slave

* 실행법

> ```
> cd slave
>
> docker build -t mypython .
>
> #푸쉬용
> docker push rehoosa/mypython
> 
> #확인용
> docker run --rm --privileged -p 80:80 mypython
>
> kubectl apply -f deployment_client.yaml
>
> ```
