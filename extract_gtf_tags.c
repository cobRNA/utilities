#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 4000

int main(int argc, char **argv)
{

    // Declara variables
    char line[MAX_LINE_LENGTH];

    // Check if tags are correctly supplied
    if (argc != 2)
    {
        printf("Usage: %s <comma-separated-strings>\n", argv[0]);
        return 1;
    }

    char *input = argv[1];
    int count = 1; // Start with 1 to account for the initial string before the first comma

    // Count the number of commas to determine the number of substrings
    for (char *p = input; *p != '\0'; p++)
    {
        if (*p == ',')
        {
            count++;
        }
    }

    // Allocate memory for the array of pointers
    char **tags = malloc(count * sizeof(char *));
    if (tags == NULL)
    {
        perror("malloc");
        return 1;
    }

    // Tokenize the input string by commas and store the substrings in the array
    char *token = strtok(input, ",");
    int i = 0;
    while (token != NULL)
    {
        tags[i++] = token;
        token = strtok(NULL, ",");
    }

    // Read line from stdin. Read till EOF
    while (fgets(line, sizeof(line), stdin))
    {
        if (line[0] != '\0')
        {
            // Remove the newline character at the end of the line, if any
            size_t len = strlen(line);
            if (len > 0 && line[len - 1] == '\n')
            {
                line[len - 1] = '\0';
            }

            // Split the line by tabs
            char *features;
            int field_count = 0;

            // Tokenize the line
            features = strtok(line, "\t");
            while (features != NULL)
            {
                field_count++;
                if (field_count == 9)
                {
                    // Exit the loop
                    break;
                }
                features = strtok(NULL, "\t");
            }

            // Check if the 9th field was found
            if (field_count < 9)
            {
                fprintf(stderr, "The input does not have at least 9 fields.\n");
                return 1;
            }

            // Search for gtf tags
            for (int j = 0; j < count; j++)
            {
                char *prefix = strcat(tags[j], " ");
                char *suffix = ";";

                // Find the start of the prefix
                char *start = strstr(features, prefix);
                if (start == NULL)
                {
                    fprintf(stderr, "Prefix not found in the input.\n");
                }
                start += strlen(prefix); // Move past the prefix

                // Find the end of the suffix
                char *end = strstr(start, suffix);
                if (end == NULL)
                {
                    fprintf(stderr, "Suffix not found in the input.\n");
                }
                *end = '\0'; // Null-terminate the substring

                // Print the extracted fragment
                printf("%s", start);
                if (j < count - 1)
                {
                    printf("\t");
                }
                        }
            // Print new line char
            printf("\n");
        }
    }
    // Free the allocated memory (not strictly necessary here since the program is terminating)
    free(tags);

    return 0;
}
