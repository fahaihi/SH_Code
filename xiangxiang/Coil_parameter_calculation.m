clear all
clc
%%
% % 罗线管线圈参数计算（基于磁场谐振耦合的无线电力传输发射及接收装置的研究 黄辉黄学良谭林林丁晓辰）
% r = 0.2; % 半径
% a = 1.4e-3; % 线径
% N = 4; % 匝数
% f = 0.9459e6; % 频率
% u0 = 4*pi*1e-7; % 真空磁导率 亨利/米
% omega = 2*pi*f; %角频率
% delta = 5.8e7; % 铜的电导率
% v = 3e8; % 真空光速
% 
% % 波的波速、波长和频率 v = lamda/T = lamda*f
% % 自感：L = u0*N^2*r*log(8*r/a-2)
% % 损耗电阻、等效欧姆电阻：R0 = sqrt(u0*omega/(2*delta))*(长度/2*pi*r)=sqrt(u0*omega/(2*delta))*(N*r/a)
% % 辐射电阻：R_rad = 320*pi^4*N^2*(pi*r^2/lamda^2)^2
% 
% lamda = v/f % 电磁波波长
% L = u0*N^2*r*(log(8*r/a-2))
% R0 = sqrt(u0*omega/(2*delta))*(N*r/a)
% R_rad = 320*pi^4*N^2*(pi*r^2/lamda^2)^2

%%
% d mm 内径
% D mm 外径
% S mm 匝间距
% N  匝数
% a  mm 导体半径
% h  mm 线圈间距
% u0 = 4*pi*1e-7 真空磁导率 亨利/米
% D = d +2*N*S 上述参数之间关系
% lamda = v/f  电磁波波长
% r = (D+d)/4 线圈中点处半径、平均半径 
% 线圈填充率β beta = (D-d)/(D+d) 
% 自感（盘型） L = u0*N*N*r*m1*(log(m2/beta)+m3*beta+m4*beta*beta);其中，拟合参数取值m1=1.0  m2=2.46  m3=0 m4=0.2
% 互感 M = (u0*pi*N1*N2*r1^2*r^2)/(2*(h^2+r1^2)^1.5)
% 金属的电导率 delta
% 损耗电阻、等效欧姆电阻：R0 = sqrt(u0*omega/(2*delta))*(长度/2*pi*r)=sqrt(u0*omega/(2*delta))*(N*r/a)
% 辐射电阻：R_rad = 320*pi^4*N^2*(pi*r^2/lamda^2)^2
% 线圈匝间电容 Ce = 0.5*pi*C0*(D+d) 其中C0为单位弧长上的电容值，与系统工作频率、电压及两线圈间距、介电常数等参数有关

%%
% % 盘形线圈自感计算（适用于无线电能传输线圈的仿真与设计教学方法）
% d = 80; % mm 内径
% D = 200; % mm 外径
% S = 4; % mm 匝间距
% N = 15; % 匝数
% a = 1.8; % mm 线径
% h = 4; % mm 线圈间距
% u0 = 4*pi*1e-7; % 真空磁导率 亨利/米
% 
% % D = d +2*N*S 上述参数之间关系
% % 线圈中点处半径 r = (D+d)/4
% % 线圈填充率β beta = (D-d)/(D+d) 
% % 自感（盘型） L = u0*N*N*r(log(2.46/beta)+0.2*beta*beta)
% % 金属的电导率 delta
% % 损耗电阻、等效欧姆电阻：R0 = sqrt(u0*omega/(2*delta))*(长度/2*pi*r)=sqrt(u0*omega/(2*delta))*(N*r/a)
% % 辐射电阻：R_rad = 320*pi^4*N^2*(pi*r^2/lamda^2)^2
% 
% 
% format long % 输出小数点位数定义
% r = (D+d)/4
% beta = (D-d)/(D+d)
% L = u0*N^2*r*(log(2.46./beta)+0.2*beta^2)




