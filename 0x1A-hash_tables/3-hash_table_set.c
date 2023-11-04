#include "hash_tables.h"
/**
 * hash_table_set - inserts an element to the hash table
 *
 * @ht: The hash table
 * @key: The key
 * @value: is the value associated with key
 *
 * Return: 1 succeed 0 otherwise
 */
int hash_table_set(hash_table_t *ht, const char *key, const char *value)
{
	unsigned long int index;
	hash_node_t *current, *node;

	/*check if the table exists*/
	if (!ht || !key || !value)
		return (0);
	index = key_index((unsigned char *)key, ht->size);
	current = ht->array[index];

	while (current != NULL)
	{
		if (strcmp(current->key, key) == 0) /*Key exists so update the value*/
		{
			free(current->value);
			current->value = strdup(value);
			if (current->value == NULL) /*updating the value failed*/
				return (0);
			return (1);
		}
	}

	node = malloc(sizeof(hash_node_t));
	if (node == NULL) /*Faile to create a new node*/
		return (0);

	node->key = strdup(key);
	if (node->key == NULL)
	{
		free(node);
		return (0);
	}

	node->value = strdup(value);
	if (node->value == NULL)
	{
		free(node->key);
		free(node);
		return (0);
	}
	node->next = ht->array[index];
	ht->array[index] = node;

	return (1);
}
