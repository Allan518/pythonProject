class GetLogs:
    def do(self, m: int, q: int, queries: []) -> None:
        records = []
        for query in queries:
            if query[0] == 'R':
                a, b, c = query.split()
                if len(records) > 0 and records[-1][1] > int(c):
                    continue
                records.append((b, int(c)))
            elif query[0] == 'G':
                temp = []
                i = len(records) - 1
                while i >= 0 and len(records) - 1 - i < m and records[-1][1] - records[i][1] < 3600:
                    temp.append(records[i][0])
                    i -= 1
                i = len(temp) - 2
                print(temp[-1], end='')
                while i >= 0:
                    print("," + temp[i], end='')
                    i -= 1
                print()
            else:
                i = len(records) - 1
                while i >= 0 and records[-1][1] - records[i][1] < 3600:
                    i -= 1
                print(len(records) - 1 - i)


so = GetLogs()
arr = ["RECORD 1 0", "RECORD 2 300", "GET_LOGS", "COUNT", "RECORD 3 1200", "RECORD 1 1800", "GET_LOGS", "COUNT",
       "RECORD 4 3900", "GET_LOGS"]
# "RECORD 1 0", "RECORD 7 600", "RECORD 3 1200", "RECORD 5 1800", "GET_LOGS", "COUNT", "RECORD 2 2400", "GET_LOGS",
#        "COUNT"
so.do(100, 10, arr)
