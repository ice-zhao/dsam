#include "rbtree.h"
#include <stdio.h>
#include <stdlib.h>


struct data_node {
    int val;
    struct rb_node d_node;
};


struct rb_root rbtree = RB_ROOT;


int rb_insert(struct data_node *node, struct rb_root *root)
{
    struct rb_node **new = &(root->rb_node), *parent = NULL;

    while(*new) {
        struct data_node *data = rb_entry(*new, struct data_node, d_node);
        parent = *new;

        if ( node->val < data->val )
            new = &((*new)->rb_left);
        else
            new = &((*new)->rb_right);
    }

    rb_link_node(&(node->d_node), parent, new);
    rb_insert_color(&(node->d_node), root);

    return 0;
}

void show_data(struct data_node* data)
{
    static const char *color[2] = {"red", "black"};
    int c = 0;

    if ( data != NULL ) {
        c = rb_color(&data->d_node);
        printf("%d,  %s\n", data->val, color[c]);
    }
}


void first_traverse(struct rb_node *root)
{
    if ( root == NULL )
        return;

    /* struct rb_node **node = &(root->rb_node); */
    struct data_node *data = rb_entry(root, struct data_node, d_node);
    show_data(data);
    first_traverse(root->rb_left);
    first_traverse(root->rb_right);
}

struct rb_node *find_node(struct rb_root *root, int val)
{
    if ( root == NULL )
        return NULL;

    struct rb_node **node = &(root->rb_node);
    struct data_node *data = NULL;

    while(*node) {
         data = rb_entry(*node, struct data_node, d_node);
         if( data->val == val )
             return *node;
         if( data->val > val )
             node = &((*node)->rb_left);
         else
             node = &((*node)->rb_right);
    }

    return *node;
}

int main()
{
    int i = 0;
    struct data_node *tmp = NULL;

    for( i = 1; i <= 6; i++ ) {
        tmp = (struct data_node*)malloc(sizeof(struct data_node));
        tmp->val = i;
        rb_insert(tmp, &rbtree);
    }

    first_traverse(rbtree.rb_node);

    struct rb_node *node = NULL;

    node = find_node(&rbtree, 3);

    printf("-----find a node to delete--------\n");
    if( node != NULL ) {
        tmp = rb_entry(node, struct data_node, d_node);
        show_data(tmp);
    }

    printf("-----after deleted--------\n");

    rb_erase(node, &rbtree);
    first_traverse(rbtree.rb_node);

    return 0;
}
