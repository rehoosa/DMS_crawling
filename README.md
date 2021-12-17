# crawling

## 차세대 분산 시스템 텀 프로젝트


* slave
* master


## slave

* 실행법

 ```
    cd slave

    docker build -t mypython .

    #푸쉬용
    docker push rehoosa/mypython
    
    #확인용
    docker run --rm --privileged -p 80:80 mypython

    kubectl apply -f deployment_client.yaml

    kubectl apply -f service.yaml

    kubectl apply -f autoscale.yaml
```

* 설명

    python alpine 버전으로 현재는 3.10.1 버전으로 생성된다.

    get 메소드로 site 와 word값을 전달받으면 url list를 넘겨준다.