#define NDEBUG

#include <bits/stdc++.h>

using namespace std;

//////////////////////
// Float comparison //
//////////////////////

#define EPSILON 0.0000001

template <typename T>
inline bool almost_equal(const T &a, const T &b) {
    return fabs(a - b) < EPSILON;
}

///////////////
// 2D Vector //
///////////////

enum Clockwise {
    PARALLEL = 1 << 0,
    CW = 1 << 1,
    CCW = 1 << 2
};  // enum Clockwise

enum Quadrant {
    ORIGIN,
    YRIGHT,
    I,
    XUP,
    II,
    YLEFT,
    III,
    XDOWN,
    IV
};  // enum Quadrant

struct Vector2 {
    Vector2() : x(0.0), y(0.0) {}
    Vector2(const double &_x, const double &_y) : x(_x), y(_y) {}

    double x, y;

    Vector2 &operator+=(const Vector2 &b) {
        x += b.x;
        y += b.y;

        return *this;
    }

    Vector2 &operator-=(const Vector2 &b) {
        x -= b.x;
        y -= b.y;

        return *this;
    }

    Vector2 &operator*=(const double &b) {
        x *= b;
        y *= b;

        return *this;
    }

    friend Vector2 operator+(const Vector2 &a, const Vector2 &b);
    friend Vector2 operator-(const Vector2 &a, const Vector2 &b);
    friend Vector2 operator*(const Vector2 &a, const double &b);

    bool operator==(const Vector2 &b) const {
        return almost_equal(x, b.x) && almost_equal(y, b.y);
    }
};  // struct Vector2

inline Vector2 operator+(const Vector2 &a, const Vector2 &b) {
    return Vector2(a.x + b.x, a.y + b.y);
}

inline Vector2 operator-(const Vector2 &a, const Vector2 &b) {
    return Vector2(a.x - b.x, a.y - b.y);
}

inline Vector2 operator*(const Vector2 &a, const double &b) {
    return Vector2(a.x * b, a.y * b);
}

inline double dot(const Vector2 &a, const Vector2 &b) {
    return a.x * b.x + a.y * b.y;
}

inline double cross(const Vector2 &a, const Vector2 &b) {
    return a.x * b.y - a.y * b.x;
}

inline double length(const Vector2 &a) {
    return sqrt(a.x * a.x + a.y * a.y);
}

inline Vector2 normalize(const Vector2 &a) {
    return a * (1.0 / length(a));
}

inline Clockwise turn(const Vector2 &u, const Vector2 &v, const Vector2 &p) {
    double result = cross(v - u, p - u);

    if (almost_equal(result, 0.0))
        return PARALLEL;
    else if (result > 0.0)
        return CCW;
    else
        return CW;
}

static Vector2 origin;

inline Quadrant detect_quadrant(const Vector2 &a) {
    Vector2 u = a - origin;

    if (u.x < 0.0) {
        if (u.y < 0.0)
            return III;
        else if (u.y > 0.0)
            return II;
        else
            return YLEFT;
    } else if (u.x > 0.0) {
        if (u.y < 0.0)
            return IV;
        else if (u.y > 0.0)
            return I;
        else
            return YRIGHT;
    } else {
        if (u.y < 0.0)
            return XDOWN;
        else if (u.y > 0.0)
            return XUP;
        else
            return ORIGIN;
    }
}

static bool cmp(const Vector2 &a, const Vector2 &b) {
    Quadrant aq = detect_quadrant(a);
    Quadrant bq = detect_quadrant(b);

    return aq < bq || (aq == bq && cross(a - origin, b - origin) > 0);
}

///////////
// Treap //
///////////

#define SEED (233)

static struct MyRandom {
    MyRandom() {
        srand(SEED);
    }

    int operator()() const {
        return rand();
    }
} randint;

struct Treap {
    Treap(const Vector2 &p)
            : vec(p)
            , left(NULL)
            , right(NULL)
            , prev(this)
            , next(this)
            , weight(randint()) {}

    Vector2 vec;
    Treap *left;
    Treap *right;
    Treap *prev;
    Treap *next;
    int weight;
};  // struct Treap

inline Treap *left_rotate(Treap *x) {
    assert(x);
    assert(x->left);

    Treap *y = x->left;
    x->left = y->right;
    y->right = x;
    return y;
}

inline Treap *right_rotate(Treap *x) {
    assert(x);
    assert(x->right);

    Treap *y = x->right;
    x->right = y->left;
    y->left = x;
    return y;
}

static Treap *insert(Treap *x, const Vector2 &p) {
    if (!x)
        return new Treap(p);

    if (cmp(p, x->vec)) {
        x->left = insert(x->left, p);

        if (x->left->prev == x->left) {
            x->prev->next = x->left;
            x->left->prev = x->prev;
            x->left->next = x;
            x->prev = x->left;
        }

        if (x->left->weight < x->weight)
            return left_rotate(x);
    } else {
        x->right = insert(x->right, p);

        if (x->right->prev == x->right) {
            x->right->next = x->next;
            x->next->prev = x->right;
            x->next = x->right;
            x->right->prev = x;
        }

        if (x->right->weight < x->weight)
            return right_rotate(x);
    }

    return x;
}

static Treap *remove(Treap *x) {
    if (!x)
        return NULL;

    if (x->left && x->right) {
        if (x->left->weight < x->right->weight) {
            Treap *y = left_rotate(x);
            y->right = remove(x);
            return y;
        } else {
            Treap *y = right_rotate(x);
            y->left = remove(x);
            return y;
        }
    } else {
        // printf("remove: Removed (%lf, %lf)\n", x->vec.x, x->vec.y);

        Treap *y = x->left ? x->left : x->right;
        x->prev->next = x->next;
        x->next->prev = x->prev;

        // delete x;

        return y;
    }
}

static Treap *remove(Treap *x, const Vector2 &p) {
    if (!x)
        return NULL;

    if (x->vec == p)
        return remove(x);
    else if (cmp(p, x->vec))
        x->left = remove(x->left, p);
    else
        x->right = remove(x->right, p);

    return x;
}

inline Treap *min_node(Treap *x) {
    while (x->left)
        x = x->left;
    return x;
}

inline Treap *max_node(Treap *x) {
    while (x->right)
        x = x->right;
    return x;
}

static Treap *lowerbound(Treap *h, const Vector2 &p) {
    Treap *y = NULL;
    Treap *x = h;

    while (x) {
        if (cmp(p, x->vec))
            x = x->left;
        else {
            y = x;
            x = x->right;
        }
    }  // while

    if (y == NULL)
        return max_node(h);
    return y;
}

/////////////////
// Convex Hull //
/////////////////

class ConvexHull {
 public:
    ConvexHull(const Vector2 &p1, const Vector2 &p2, const Vector2 &p3)
            : convex(NULL) {
        origin = { (p1.x + p2.x + p3.x) / 3.0, (p1.y + p2.y + p3.y) / 3.0 };
        convex = insert(convex, p1);
        convex = insert(convex, p2);
        convex = insert(convex, p3);
    }

    void insert_point(const Vector2 &p) {
        if (contain(p))
            return;

        Treap *u = lowerbound(convex, p);
        Treap *v = u->next;

        assert(u);
        assert(v);

        // printf("u = (%lf, %lf), v = (%lf, %lf)\n", u->vec.x, u->vec.y,
        // v->vec.x,
        // v->vec.y);
        // puts("Check forward...");
        while (turn(p, u->vec, u->prev->vec) & (CCW | PARALLEL)) {
            u = u->prev;
            convex = remove(convex, u->next->vec);

            assert(u);
        }

        // puts("Check backwards...");
        while (turn(p, v->vec, v->next->vec) & (CW | PARALLEL)) {
            v = v->next;
            convex = remove(convex, v->prev->vec);

            assert(v);
        }

        convex = insert(convex, p);
    }

    bool contain(const Vector2 &p) {
        if (p == origin)
            return true;

        Treap *u = lowerbound(convex, p);
        return turn(u->vec, u->next->vec, p) & (CCW | PARALLEL);
    }

 private:
    Treap *convex;
};  // class ConvexHull

static int q;
static Vector2 p1, p2, p3;
static ConvexHull *convex;

static void initialize() {
    int _;

    scanf("%d", &q);
    scanf("%d%lf%lf", &_, &p1.x, &p1.y);
    scanf("%d%lf%lf", &_, &p2.x, &p2.y);
    scanf("%d%lf%lf", &_, &p3.x, &p3.y);
    q -= 3;

    convex = new ConvexHull(p1, p2, p3);
}

int main() {
    initialize();

    while (q--) {
        int type, x, y;
        scanf("%d%d%d", &type, &x, &y);

        if (type == 1)
            convex->insert_point(Vector2(x, y));
        else
            puts(convex->contain(Vector2(x, y)) ? "YES" : "NO");

        // printf("Completed %d %d %d.\n", type, x, y);
    }  // while

    return 0;
}  // function main
