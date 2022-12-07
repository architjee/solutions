n, m = map(int, input().split())
n_length, m_length = [], []
n_speed , m_speed = [], []

for _ in range(n):
    length, speed = map(int, input().split())
    n_length.append(length)
    n_speed.append(speed)
n_length.append(0)
n_speed.append(0)
for _ in range(m):
    length, speed = map(int, input().split())
    m_length.append(length)
    m_speed.append(speed)
m_length.append(0)
m_speed.append(0)
n_ptr = 0
m_ptr = 0
overspeed = 0
length_of_x=n_length[0]
length_of_y = m_length[0]
while n_ptr < n and m_ptr<m:
    overspeed = max(overspeed, m_speed[m_ptr]-n_speed[n_ptr])
    if length_of_x<length_of_y:
        # We will attempt to move n only
        ## Move n
        n_ptr+=1
        length_of_x += n_length[n_ptr]

        pass
    elif length_of_x>length_of_y:
        # We will attempt to move m only
        ## Move m
        m_ptr+=1
        length_of_y += m_length[m_ptr]
    else:
        ## Move both simultaneously.
        n_ptr+=1
        m_ptr+=1
        length_of_x += n_length[n_ptr]
        length_of_y += m_length[m_ptr]
print(overspeed)