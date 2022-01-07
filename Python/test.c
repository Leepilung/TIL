	/*-------------------------- project.2-Parsing -----------------------------*/
	/* file_name을 사용해야 하는데, f_name을 공백 기준으로 쪼개야 한다. 
	또한 이 과정에서 file_name 원본은 아래에서 사용되므로 깊은 복사(memcpy)로 복사본을 만들 필요가 있다. */
	char *file_name_copy[48];
	
	/* strlen에서 +1 해주는 이유 : strlen함수 들어가보면 '\0(\n)'을 만나면 동작을 중지한다.
	그러나 우리는 콘솔창에서 명령어를 입력하고 엔터를 치게되면 자동으로 명령어 끝에 '\n'이 들어간다.
	각 문자열 단위마다 '\n'을 추가해준 만큼 4 1 1 의 구성이 5 2 2로 바뀌기 떄문에 문자열의 총 byte가 8을 넘어가면 더블워드 단위이기 때문에
	9byte로 8byte 단위를 넘기 떄문에 7byte의 더미를 추가해줘야 한다. 고로 8byte가 추가된다고 보면된다. */
	memcpy(file_name_copy, file_name, strlen(file_name) +1 );

	/* arg_list라는 배열을 만들고, 각 인자의 *char를 담아준다. 
	ex: 프로그램 명 -> arg_list[0], 2번째 인자는 arg_list[1] */
	char *token, *last;
	char *arg_list[64];
	int token_count = 0;

	token = strtok_r(file_name_copy, " ", &last); // strok_r : 문자열을 공백단위로 슬라이싱 해주는 함수.
	char *tmp_save = token;	// 초기값 저장
	arg_list[token_count] = token;	// 각 token_count 인덱스에 token값 저장
	while (token != NULL)
	{
		token = strtok_r(NULL, " ",&last);
		token_count++;
		arg_list[token_count] = token;
	}

	/* And then load the binary */
	success = load (tmp_save, &_if);
	
	/* If load failed, quit. */
	palloc_free_page (file_name);
	if (!success)
	{
		return -1;
	}

	argument_stack(arg_list, token_count, &_if);
    /*-------------------------- project.2-Parsing -----------------------------*/
	hex_dump(_if.rsp, _if.rsp, USER_STACK - _if.rsp, true);
	
	// /* Start switched process. */
	// do_iret (&_if);
	// NOT_REACHED ();
}

void argument_stack(char **argv, int argc, struct intr_frame *if_)
/* **argv : 저장한 인자의 배열(arg_list), argc : 인자의 갯수 
ex) '/bin/ls -l foo bar'가 입력됐따면, arg_list에는 [/bin/ls\0, -l\0, foo\0, bar\0]가 담겨있다고 가정하면
argv는 [/bin/ls\0, -l\0, foo\0, bar\0]를 가리키는 포인터가 되고, argc는 4가 된다. */
{
    /* insert arguments' address */
    char *argu_address[128];
    for (int i = argc - 1; i >= 0; i--)
    {
        int argv_len = strlen(argv[i]);
        if_->rsp -= (argv_len + 1);
		// if->rsp : 현재 user stack에서 현재 위치를 가리키는 스택 포인터(stack pointer)
		// 각 인자에서 인자의 크기를 읽고( 각 인자에는 sentinel이 포함되있기 떄문에 strlen +1)
		// 그 크기만큼 rsp를 내려주고
		
		// rsp에 인자를 복사시킨다(memcpy)
        memcpy(if_->rsp, argv[i], argv_len + 1); // 확보한 공간에 문자열 추가

		argu_address[i] = if_->rsp; // 스택에 추가된 문자열의 주소값을 보관한다.
    }
    
    /* insert padding for word-align */
    while (if_->rsp % 8 != 0)
    {
        if_->rsp--;
        *(uint8_t *)(if_->rsp) = 0;
    }
    
    /* insert address of strings including sentinel */
    for (int i = argc; i >= 0; i--)
    {
        if_->rsp = if_->rsp - 8;
        if (i == argc)
            memset(if_->rsp, 0, sizeof(char **));
        else
            memcpy(if_->rsp, &argu_address[i], sizeof(char **));
    }
    
    /* fake return address */
    if_->rsp -= 8;
    memset(if_->rsp, 0, sizeof(void *));

    if_->R.rdi = argc;
    if_->R.rsi = if_->rsp + 8;

	
}	
