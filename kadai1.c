/* 2064271 Mori Yugo */

#include <stdio.h>
#include <math.h>

int main(void){
	int i;
	float S1,S2,t,t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,max,min,ave,bun,hyo,hen;
	FILE *fp1;
	i=0;
	S1=0.0;
	S2=0.0;
	max=-999.99;
	min=999.99;
	
	fp1=fopen("temperature.txt","r");
	while(fscanf(fp1,"%d %f %f %f %f %f %f %f %f %f %f",&t,&t1,&t2,&t3,&t4,&t5,&t6,&t7,&t8,&t9,&t10)==11){
		if(t3<999){
			i=i+1;
			S1=S1+t3;
			S2=S2+t3*t3;
				if(max<t3){
					max=t3;
				}
				if(min>t3){
					min=t3;
				}
		}
	}
	fclose(fp1);
	ave=S1/i;
	bun=S2/i-ave*ave;
        hyo=sqrt(bun);
	hen=(14.6-ave)*10.0/hyo+50;
	printf("data=%d\n",i);
	printf("max=%f\n",max);
	printf("min=%f\n",min);
	printf("average=%f\n",ave);
	printf("bunsan=%f\n",bun);
	printf("hyoujunhensa=%f\n",hyo);
	printf("2019 no hensati=%f\n",hen);
	return 0;
}

/*
C:\Users\youwu\OneDrive\ドキュメント\プログラミング実習>kadai1
data=138
max=14.900000
min=11.700000
average=13.121015
bunsan=0.513992
hyoujunhensa=0.716933
2019 no hensati=70.629349
*/
