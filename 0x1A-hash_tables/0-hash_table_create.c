#include "hash_tables.h"

/**
 * hash_table_create - This function creates a hash table
 * with size @size
 * @size: The size of the table
 *
 * Returns: a hash_table_t otherwise NULL
 */
hash_table_t *hash_table_create(unsigned long int size)
{
	unsigned long int i;

	/*Create the table*/
	hash_table_t *table = malloc(sizeof(hash_table_t));

	if (!table)
		return (NULL);

	table->size = size;
	table->array = malloc(size * sizeof(hash_node_ti *));
	
	if (!table->array)
	{
		free(table);
		return (NULL);
	}

	for (i = 0; i < size; i++)
	{
		table->array[i] = NULL;
	}

	return (table);
}
