class chained
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity     # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key,int):                 # key가 int형인 경우 해당.
                return key % self.capacity
        return(int(hashlib.sha256(str(key).endcode()).hexdigest(), 16) % self.capacity)     # 표준 라이브러리 사용 예
        #haslib에서 sha256을 사용하여 바이트 문자열의 해시값을 구하는 해시 알고리즘 생성자를 생성한다.
        # 그 뒤에 hashlib.sah256에 바이트 문자열의 인수를 전달해야 하므로 key를 str형 문자열로 변환한 뒤, 그 문자열을 encode() 함수에 전달
        # hexdigest()함수는 sha 256 알고리즘에서 해시값을 16진수 문자열로 꺼낸다.
        # int()함수 : hexdigest()함수로 꺼낸 문자열을 16진수 문자열로 하는 int형으로 변환한다.
 