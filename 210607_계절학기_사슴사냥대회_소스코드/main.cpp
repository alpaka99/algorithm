#define DEER 0
#define RABBIT 1
#define SNAKE 2

#include <stdio.h>
#include <algorithm>
#include <assert.h>
#include <time.h>
using namespace std;


// 아래 Me함수를 작성해서 제출하세요.
//int Me(int opp, int turn, int opp_prev, int opp_last_pattern[][10])
//{
//	//// ToDO
//}

int Opponent1(int opp, int turn, int opp_prev, int opp_last_pattern[][10])
{
	return 0;
}

int Opponent2(int opp, int turn, int opp_prev, int opp_last_pattern[][10])
{
	if (turn == 0) return 1;
	return opp_prev;
}

int Opponent3(int opp, int turn, int opp_prev, int opp_last_pattern[][10])
{
	if (turn == 0) return 2;
	return opp_prev;
}

typedef int EntryFunction(int opp, int turn, int opp_prev, int opp_last_pattern[][10]);

EntryFunction* f[150] = { 0 };
const char* names[100];
int f_inx = 0;
int total_score[150];
int last_pattern[150][150][10]; // [팀][대전][패턴]
int pattern_count[150];

void Register(const char* name, EntryFunction func)
{
	names[f_inx] = name;
	f[f_inx++] = func;
}


void main(void)
{
	srand((unsigned int)time(NULL));

	//Register("Me", Me);

	Register("Opp1", Opponent1);
	Register("Opp2", Opponent2);
	Register("Opp3", Opponent3);

	for (int i = 0; i < 140; i++)for (int j = 0; j < 140; j++) for (int k = 0; k < 10; k++) last_pattern[i][j][k] = -1;

	for (int i = 1; i < f_inx; i++)
	{
		for (int j = 0; j < f_inx; j++) {
			int team_a = j % f_inx; // 여기부터 i, j를 team_a, team_b로 바꿔줘야됨
			int team_b = (j + i) % f_inx;
			printf("[%s] vs [%s]\n", names[team_a], names[team_b]);

			int a_game_score = 0;
			int b_game_score = 0;

			int prev_a = -1;
			int prev_b = -1;

			int team_a_cont = 0;
			int team_b_cont = 0;

			int a_pattern[10];
			int b_pattern[10];

			for (int k = 0; k < 10; k++)
			{
				printf("<turn %d>\n", k);
				int a = f[team_a](team_b, k, prev_b, last_pattern[team_b]);
				int b = f[team_b](team_a, k, prev_a, last_pattern[team_a]);
				a_pattern[k] = a;
				b_pattern[k] = b;

				if (a == prev_a) team_a_cont += a + 1; else team_a_cont = 0;
				if (b == prev_b) team_b_cont += b + 1; else team_b_cont = 0;

				if (a != 0 && a != 1 && a != 2) team_a_cont = 100;
				if (b != 0 && b != 1 && b != 2) team_b_cont = 100;

				prev_a = a;
				prev_b = b;

				int a_score;
				int b_score;

				if (a == DEER && b == DEER) a_score = 50, b_score = 50;
				else if (a == DEER && b == RABBIT) a_score = 0, b_score = 20;
				else if (a == DEER && b == SNAKE) a_score = 0, b_score = 10;
				else if (a == RABBIT && b == DEER) a_score = 20, b_score = 0;
				else if (a == RABBIT && b == RABBIT) a_score = 20, b_score = 20;
				else if (a == RABBIT && b == SNAKE) a_score = 0, b_score = 30;
				else if (a == SNAKE && b == DEER) a_score = 10, b_score = 0;
				else if (a == SNAKE && b == RABBIT) a_score = 30, b_score = 0;
				else if (a == SNAKE && b == SNAKE) a_score = 10, b_score = 10;

				a_score -= team_a_cont, b_score -= team_b_cont;
				a_score += rand() % 3;
				b_score += rand() % 3;

				a_game_score += a_score;
				b_game_score += b_score;

				printf("[%4s] : %s, [%4s] : %s\n", names[team_a], a ? (a == 2 ? "SNAKE" : "RABBIT") : "DEER",
					names[team_b], b ? (b == 2 ? "SNAKE" : "RABBIT") : "DEER");
				printf("[%4s] score:  This turn:%5d, Game score:%5d, Total score:%5d\n",
					names[team_a], a_score, a_game_score, total_score[team_a] + a_game_score);
				printf("[%4s] score:  This turn:%5d, Game score:%5d, Total score:%5d\n",
					names[team_b], b_score, b_game_score, total_score[team_b] + b_game_score);
			}
			for (int z = 0; z < 10; z++) last_pattern[team_a][pattern_count[team_a]][z] = a_pattern[z];
			for (int z = 0; z < 10; z++) last_pattern[team_b][pattern_count[team_b]][z] = b_pattern[z];
			pattern_count[team_a] ++;
			pattern_count[team_b] ++;
			printf("<game result>\n");
			if (a_game_score == b_game_score) printf("Draw\n");
			else printf("Win: [%4s]!\n", a_game_score > b_game_score ? names[team_a] : names[team_b]);
			printf("\n");
			total_score[team_a] += a_game_score;
			total_score[team_b] += b_game_score;

		}
	}

	printf("<Final score>\n");
	int max_inx = 0;
	int max_score = 0;
	for (int i = 0; i < f_inx; i++)
	{
		printf("[%4s] Total Score: %d\n", names[i], total_score[i]);
		if (max_score < total_score[i])
			max_inx = i, max_score = total_score[i];
	}

	printf("<Winner: [%4s]!!!!>\n", names[max_inx]);
	printf("%d\n", max_score);
	int sdf = 1;
}

