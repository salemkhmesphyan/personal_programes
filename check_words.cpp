#include<iostream>
//#include<conio.h>
/*
 يفحص الكلام او الجملة المدخلة اذا فيها تكراربعض الحروف يطبع ) او ( * 
 * 
"""
programmer by en:salem khmes phyan
""" * 
 * 
 */
using namespace std;
int main(){
int m;
int r=0;
cout<<"enter number charcters in words:";
cin>>m;
cout<<"\n";
char ss[m];
cout<<"enter in words:";
cin>>ss;
for(int i=0;i<m;i++){
	for(int j=0;j<m;j++){
	if (ss[i]==ss[j]){
		r+=1;
		}
	}
	if (r>1){
		cout<<")";
		r=0;
		}
		else{
			cout<<"(";
			r=0;
			}}
//cout<<ss;
//getch();
return 0;}
