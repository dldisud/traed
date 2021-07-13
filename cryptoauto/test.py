import pyupbit

access = "J2uvBQSScT3xIVTXYGxCChD8NXneinvo5mQACgxy"          # 본인 값으로 변경
secret = "e4XG6xxHSJlxcaUMf7tx5NVrZ7kxg4LleBW1QOcD"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC, KRW-SBD"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회