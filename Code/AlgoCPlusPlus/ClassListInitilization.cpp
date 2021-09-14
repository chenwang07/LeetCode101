class B
{
public:
    B(int _b)
    {
        b = _b;
    }

private:
    int b;
};


class A
{
public:
    A(int _a)
    {
        a = _a;
    }

private:
    int a;
};

//在对象构建过程中，如果有构造函数初始化列表，首先执行初始化列表中的内容，然后执行构造函数。并且，初始化列表中数据的构造顺序并不是按照在初始化列表中的先后顺序进行的，而是根据初始化列表中数据所在当前类中的定义顺序决定的。

class C
{
public:
    C(int _c, int _a, int _b) :v_b(_b), v_a(_a)
    {
        c = _c;
    }
private:
    int c;
    A v_a;

    B v_b;
};



    //C object_c(1, 2, 3);
    //getchar();