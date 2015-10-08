#C++经验技巧

unordered_map



```
//读取文件
char *read_file(char *path, int *psize)
{   
    char *buffer = NULL;
    FILE *file = fopen(path, "r");
    if (file) {
        fseek(file, 0, SEEK_END);
        int size = ftell(file);
        if (size > 0) {
            fseek(file, 0, SEEK_SET);
            buffer = malloc(size);
            *psize = fread(buffer, 1, size, file);
        }
        fclose(file);
    }
    return buffer;
}
 

//写入文件
int write_to(char *path, char *buffer, int size)
{
    int result = 0;
    FILE *file = fopen(path, "w");
    if (file) {
        result = fwrite(buffer, 1, size, file);
        fclose(file);
    }
    return result;
}
```