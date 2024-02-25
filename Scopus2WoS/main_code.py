import pandas as pd
import datetime
import matplotlib.pyplot as plt
from datetime import date

# Specify the working directory and file path

#file_path = "C:/Users/markb/OneDrive/Vlado/scopus/handball_scopus.csv"
file_path = "C:/Users/markb/OneDrive/Vlado/scopus/test.csv"

print(file_path)
# Read the CSV file into a DataFrame

SF = pd.read_csv(file_path, header=None, skiprows=[0])
print(SF.head(10))

# Define the short column names
short = ["au", "aufull", "IDa", "tit", "y", "jour", "vol", "iss", "art", "beg",
         "end", "np", "cite", "DOI", "URL", "aff", "awaff", "abs", "akey", "indkey",
         "ref", "corr", "edi", "pub", "spo", "conn", "cond", "conl", "conc", "ISSN", "ISBN", "CODEN", "pmID", "lan",
         "abb", "dt", "ps", "oa", "sour", "EID"]

# Set the column names of the DataFrame
SF.columns = short

# Get the number of rows in SF
n = len(SF) # number of rows
nc = len(short) # number of columns

# Set the size parameters
step = 5000
N = 15 * n # 15 is expected in advance

# Create empty DataFrame A to fill it with our new values afterwards
A = pd.DataFrame({'work': [None] * N,
                  'IDa': [None] * N,
                  'au': [None] * N,
                  'y': [None] * N})

k = -1
current_work = 1  # Initialize the current work number

print("Start", datetime.datetime.now(), ", n =", n)

# Loop through each row in SF
for w in range(n):
    # Extract 'au' and 'IDa' values
    ans = str(SF['au'][w]).replace(".", "").split("; ")
    ais = str(SF['IDa'][w]).split("; ")
    year = int(SF["y"][w])
    print(w, ans, ais, year)

    # Check if the lengths of ans and ais are equal
    if len(ans) == len(ais):
        for i in range(len(ans)):
            k += 1
            if (k % step == 0) and (w > 0):
                print(datetime.datetime.now(), " w =", w, "  k =", k, " k/w =", k / w)
            if k > N:
                raise ValueError("increase size N, w=" + str(w))
            A.loc[k, 'work'] = current_work
            A.loc[k, 'IDa'] = ais[i]
            A.loc[k, 'au'] = f"'{ans[i]}'"
            A.loc[k, 'y'] = year
            #print(A.loc[k - 1, 'work'], A.loc[k - 1, 'IDa'], A.loc[k - 1, 'au'])
    else:
        print("Warning: work", w)

    # Update the current work number
    current_work += 1

print("Stop", datetime.datetime.now(), ", k =", k, ", k/n =", k / n)

#print(A.head())
print(A[0:(k+1)])

A = A[0:k] # to see the rights

# frequency of frequencies for the 'work' column
Wd = A['work'].value_counts().value_counts().sort_index()
print(Wd)


# plot Number of authors per paper distribution
x = Wd.index.astype(float)
plt.scatter(x, Wd, marker='o', s=10, c='blue', alpha=0.7)
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('Authors')
plt.ylabel('Frequency')
plt.title('Handball - Number of authors per paper distribution')
#plt.show()

# frequency of frequencies for the 'IDa' column
Id = A['IDa'].value_counts().value_counts()

# Plot for works per author
x = Id.index.astype(float)
plt.scatter(x, Id, marker='o', s=10, c='blue', alpha=0.7)
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('Works')
plt.ylabel('Freqency')
plt.title('Handball - Number of works per author distribution')
#plt.show()

#
I = pd.Categorical(A['IDa']) # pd.Categorical function is used to create a factor variable I
L = I.categories # unique levels for IDs
Ia = I.codes.astype(int) # integer codes
nA = len(L) # length of levels

Anam = [None] * nA
Anam_dict = dict(zip(L, Anam))

# checking if some authors appear in the data with different names
for i in range(len(A)):
    nam = A['au'][i]
    ID = A['IDa'][i]

    if Anam_dict[ID] is None:
        Anam_dict[ID] = nam
    elif Anam_dict[ID] != nam:
        print(f"Warning: {ID}: {nam}/{Anam_dict[ID]}")



# Use a different placeholder for the dictionary
CN = A['IDa'].unique()
Anam_dict = dict(zip(CN, [None] * len(CN)))


with open("WA.net", "w", encoding="UTF-8") as net:
    RN = SF['EID']
    nr = len(RN)
    CN = L
    nc = len(CN)
    U = A['work']
    V = Ia
    w = [1] * len(U)
    t = A['y']

    net.write("% CSV2Pajek " + str(date.today()) + "\n*vertices " + str(nr + nc) + " " + str(nr) + "\n")

    for i in range(nr):
        net.write(str(i + 1) + ' "' + str(RN[i]) + '"\n')

    for i in range(nc):
        net.write(str(i + nr + 1) + ' "' + str(CN[i]) + '"\n')

    net.write("*arcs\n")

    for i in range(len(U)):
        net.write(str(U[i]) + ' ' + str(V[i] + nr) + ' ' + str(w[i]) + ' [' + str(t[i]) + ']\n')

# Using authors.nam we can replace in Pajek the author IDs with the corresponding names and get more readable results
with open("authors.nam", "w", encoding="UTF-8") as nam:
    nam.write("% CSV2Pajek " + str(date.today()) + "\n*vertices " + str(len(CN)) + "\n")

    for i, cn in enumerate(CN):
        nam.write(str(i + 1) + ' "' + str(Anam_dict.get(cn, 'Unknown')) + '"\n')

print("Done")

def stand(s): # s represents author names separated by commas
    p = s.split(", ") # splits the string into a list
    k = len(p)
    if k > 1: # checks if the list has more than one element
        p[k - 1] = p[k - 1].replace("-", "")
    else:
        p.append("")
        k = 2 # if there is only one element in the list, it appends an empty string to it, and sets k to 2
    return {"k": k, "p": p} # returns a dictionary with keys "k" and "p,"
    # representing the count of elements (k) and the modified list (p)

I = pd.Categorical(A['IDa'])
L = I.categories
Ia = I.codes.astype(int)

Anam = pd.Series([None] * len(L), index=L)

for i in range(len(A)):
    ID = A['IDa'][i]
    b = stand(A['au'][i])
    nam = ", ".join(b['p'])
    if pd.isna(Anam[ID]):
        Anam[ID] = nam
    elif Anam[ID] != nam:
        a = stand(Anam[ID])
        na = len(a['p'][a['k'] - 1])
        nb = len(b['p'][b['k'] - 1])
        if nb > na:
            print(f"Warning: {i} {ID}: {A['au'][i]}/{Anam[ID]}")
            Anam[ID] = nam

with open("authors2.nam", "wb") as nam:
    nam.write('\xEF\xBB\xBF'.encode())  # BOM (Byte Order Mark)
    nam.write(f"% CSV2Pajek {date.today()}\n*vertices {len(L)}\n".encode())
    for i, name in enumerate(L):
        nam.write(f"{i + 1} \"{Anam[name]}\"\n".encode())







