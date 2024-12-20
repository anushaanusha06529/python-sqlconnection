def create_co():
    import sqlite3
    DBCO=sqlite3.connect('Anu.db')
    return DBCO
DBCO=create_co()


def create_table(DBCO):
    CRO=DBCO.cursor()
    CRO.execute('create table dept(dno int primary key,dname text)')
    DBCO.commit()
    print('table is created')
create_table(DBCO)    
                
def insert_data(DBCO):
    CRO=DBCO.cursor()
    CRO.execute('insert into dept values(143,"Anu")')
    DBCO.commit()
    print('data inserted')

insert_data(DBCO)

          
def retrieve_data(DBCO):
    CRO=DBCO.cursor()
    QUERYSET=CRO.execute('select * from dept')
    for i in QUERYSET:
        print(i)
retrieve_data(DBCO)


def update_data(DBCO):
    CRO=DBCO.cursor()
    CRO.execute('update dept set dname="seenu" where dno=143)')
    DBCO.commit()
    print('updation of data done')
update_data(DBCO)
retrieve_data(DBCO)

def delete_data(DBCO):
    CRO=DBCO.cursor()
    CRO.execute('delete from dept where dno=143')
delete_data(DBCO)
retrieve_data(DBCO)
