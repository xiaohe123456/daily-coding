#include <stdio.h>
#include <stdlib.h>
#define TBL_SIZE(a) ( (sizeof(a)) / (sizeof(a[0])) )

typedef int Type;
typedef struct BSTreeNode{
    Type   key;                    // �ؼ���(��ֵ)
    int layer;
 struct BSTreeNode *left;    // ����
 struct BSTreeNode *right;    // �Һ���
 struct BSTreeNode *parent;    // �����
}Node, *BSTree;



/*
 * (�ݹ�ʵ��)����"������x"�м�ֵΪkey�Ľڵ�
 */
Node* bstree_search(BSTree x, Type key)
{
 if (x==NULL || x->key==key)
    return x;
 if (key < x->key)
    return bstree_search(x->left, key);
 else
    return bstree_search(x->right, key);
}
/*
 * (�ǵݹ�ʵ��)����"������x"�м�ֵΪkey�Ľڵ�
 */
Node* iterative_bstree_search(BSTree x, Type key)
{
    while ((x!=NULL) && (x->key!=key))
    {
        if (key < x->key)
            x = x->left;
        else
            x = x->right;
    }
    return x;
}
/*
 * ������С��㣺����treeΪ�����Ķ���������С��㡣
 */
Node* bstree_minimum(BSTree tree)
{
    if (tree == NULL)
        return NULL;
    while(tree->left != NULL)
        tree = tree->left;
    return tree;
}
/*
 * ��������㣺����treeΪ�����Ķ�����������㡣
 */
Node* bstree_maximum(BSTree tree)
{
    if (tree == NULL)
        return NULL;
    while(tree->right != NULL)
        tree = tree->right;
    return tree;
}
/*
 * �ҽ��(x)�ĺ�̽�㡣��������"������������ֵ���ڸý��"��"��С���"��
 */
Node* bstree_successor(Node *x)
{
    // ���x�����Һ��ӣ���"x�ĺ�̽��"Ϊ "�����Һ���Ϊ������������С���"��
    if (x->right != NULL)
        return bstree_minimum(x->right);
  // ���xû���Һ��ӡ���x���������ֿ��ܣ�
  // (01) x��"һ������"����"x�ĺ�̽��"Ϊ "���ĸ����"��
  // (02) x��"һ���Һ���"�������"x����͵ĸ���㣬���Ҹø����Ҫ��������"���ҵ������"��͵ĸ����"����"x�ĺ�̽��"��
    Node* y = x->parent;
    while ((y!=NULL) && (x==y->right))
    {
        x = y;
        y = y->parent;
    }
    return y;
}
/*
 * �ҽ��(x)��ǰ����㡣��������"������������ֵС�ڸý��"��"�����"��
 */
Node* bstree_predecessor(Node *x)
{
    // ���x�������ӣ���"x��ǰ�����"Ϊ "��������Ϊ���������������"��
    if (x->left != NULL)
        return bstree_maximum(x->left);
    // ���xû�����ӡ���x���������ֿ��ܣ�
    // (01) x��"һ���Һ���"����"x��ǰ�����"Ϊ "���ĸ����"��
    // (01) x��"һ������"�������"x����͵ĸ���㣬���Ҹø����Ҫ�����Һ���"���ҵ������"��͵ĸ����"����"x��ǰ�����"��
    Node* y = x->parent;
    while ((y!=NULL) && (x==y->left))
    {
        x = y;
        y = y->parent;
    }
    return y;
}
/*
 * ���������ض�������㡣
 *
 * ����˵����
 *     key �Ǽ�ֵ��
 *     parent �Ǹ���㡣
 *     left �����ӡ�
 *     right ���Һ��ӡ�
 */
static Node* create_bstree_node(Type key, Node *parent, Node *left, Node* right)
{
    Node* p;
    if ((p = (Node *)malloc(sizeof(Node))) == NULL)
        return NULL;
    p->key = key;
    p->left = left;
    p->right = right;
    p->parent = parent;
    //push(p);

    return p;
}
/*
 * �������뵽��������
 *
 * ����˵����
 *     tree �������ĸ����
 *     z ����Ľ��
 * ����ֵ��
 *     ���ڵ�
 */
static Node* bstree_insert(BSTree tree, Node *z)
{
    Node *y = NULL;
    Node *x = tree;
    // ����z�Ĳ���λ��
    while (x != NULL)
    {
        y = x;
        if (z->key < x->key)
            x = x->left;
        else
            x = x->right;
    }
    z->parent = y;
    if (y==NULL)
        tree = z;
    else if (z->key < y->key)
        y->left = z;
    else
        y->right = z;
    return tree;
}
/*
 * �½����(key)����������뵽��������
 *
 * ����˵����
 *     tree �������ĸ����
 *     key ������ļ�ֵ
 * ����ֵ��
 *     ���ڵ�
 */
Node* insert_bstree(BSTree tree, Type key)
{
    Node *z;    // �½����
    // ����½����ʧ�ܣ��򷵻ء�
    if ((z=create_bstree_node(key, NULL, NULL, NULL)) == NULL)
        return tree;
    return bstree_insert(tree, z);
}
/*
 * ɾ�����(z)�������ظ��ڵ�
 *
 * ����˵����
 *     tree �������ĸ����
 *     z ɾ���Ľ��
 * ����ֵ��
 *     ���ڵ�
 */
static Node* bstree_delete(BSTree tree, Node *z)
{
    Node *x=NULL;
    Node *y=NULL;
    if ((z->left == NULL) || (z->right == NULL) )
        y = z;
    else
        y = bstree_successor(z);
    if (y->left != NULL)
        x = y->left;
    else
        x = y->right;
    if (x != NULL)
        x->parent = y->parent;
    if (y->parent == NULL)
        tree = x;
    else if (y == y->parent->left)
        y->parent->left = x;
    else
        y->parent->right = x;
    if (y != z)
        z->key = y->key;
    if (y!=NULL)
    free(y);
    return tree;
}
/*
 * ɾ�����(keyΪ�ڵ�ļ�ֵ)�������ظ��ڵ�
 *
 * ����˵����
 *     tree �������ĸ����
 *     z ɾ���Ľ��
 * ����ֵ��
 *     ���ڵ�
 */
Node* delete_bstree(BSTree tree, Type key)
{
    Node *z, *node;
    if ((z = bstree_search(tree, key)) != NULL)
        tree = bstree_delete(tree, z);
    else
        printf("�����ݲ�����\n");
    return tree;
}
/*
 * ���ٶ�����
 */
void destroy_bstree(BSTree tree)
{
    if (tree==NULL)
        return ;
    if (tree->left != NULL)
        destroy_bstree(tree->left);
    if (tree->right != NULL)
        destroy_bstree(tree->right);
        free(tree);
}
/*
 * ��ӡ"������"
 *
 * tree       -- �������Ľڵ�
 * key        -- �ڵ�ļ�ֵ
 * direction  --  0����ʾ�ýڵ��Ǹ��ڵ�;
 *               -1����ʾ�ýڵ������ĸ���������;
 *                1����ʾ�ýڵ������ĸ������Һ��ӡ�
 */
void print_bstree(BSTree tree, Type key, int direction)
{
    if(tree != NULL)
    {
        if(direction==0)  // tree�Ǹ��ڵ�
            printf("%2d is root\n", tree->key);
        else  // tree�Ƿ�֧�ڵ�
            printf("%2d is %2d's %6s child\n", tree->key, key, direction==1?"right" : "left");
        print_bstree(tree->left, tree->key, -1);
        print_bstree(tree->right,tree->key,  1);
    }
}






//static int arr[];
void main()
{
    int maxsize;
    printf("���������ݸ���\n");
    scanf("%d", &maxsize);
    int arr[maxsize];
    printf("��������������Ԫ��\n");

    int i, ilen;
    for(i=0; i<maxsize; i++)
    {
        scanf("%d", &arr[i]);
    }
    Type data;
    BSTree root=NULL;
    BSTree root1=NULL;
    ilen = TBL_SIZE(arr);
    for(i=0; i<ilen; i++)
    {
        printf("%d ", arr[i]);
        root = insert_bstree(root, arr[i]);
    }

    printf("\n== ������ϸ��Ϣ: \n");
    print_bstree(root, root->key, 0);
    int deleteData;

    printf("������Ҫɾ��������\n");
    scanf("%d", &deleteData);
    root = delete_bstree(root, deleteData);
    printf("== ������ϸ��Ϣ: \n");
    print_bstree(root, root->key, 0);
    printf("��������: \n");
    scanf("%d", &data);
    root = insert_bstree(root, data);
    printf("== ������ϸ��Ϣ: \n");
    print_bstree(root, root->key, 0);
    printf("���ҵ�����: \n");
    scanf("%d", &data);
    root1 = iterative_bstree_search(root, data);
    if(root1 == NULL)
        printf("����ʧ��");
    else
        printf("���ҳɹ�");

    //printf("\n== �������: ");
    //inorder_bstree(root);
    printf("\n");
    // ���ٶ�����
    destroy_bstree(root);
}




