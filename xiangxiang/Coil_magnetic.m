%% 导线周围电磁场动态
% i = 1;
% [a,z]=ndgrid((0:0.01:1)*2*pi,-10:0.2:10);
% x=i*cos(a);
% y=i*sin(a);
% for t = 0:1:100
% Hx = sin(a)*1.25/(pi*(1+i))*cos(-0.5*z+t);
% Hy = -cos(a)*1.25/(pi*(1+i))*cos(-0.5*z+t);
% surf(x,y,z)
% hold on
% plot3(Hx,Hy,z);
% hold off
% f=getframe(gcf);
% imwrite(f.cdata,['D:\workspace\',int2str(t),'.jpg']);
% end
%% 载流线圈的磁感应强度
% NMAX = 1000;
% Q = 1; %总电荷
% a = 10; %圆盘半径
% I0 = 1; %电流
% U0 = 4*pi*1e-7; %真空磁导率
% % 一下两行数据，第一行为半径r的不同取值，第二行为角度xeta的不同取值，同一列代表一个计算点（r,xeta)
% % 每行必须以0结束，这些数据可以任意修改，或增加计算点
% RR = [100,1000,10000,1000000, 10000,10000,10000,0];
% XX = [0,0,0,0.52359936667,0.2,0.5,1.0,0];
% disp(' ')
% disp('参数取值：')
% disp(['',' 圆电流半径 R=',num2str(a),',','总电荷Q=',num2str(Q),',','电流I=',num2str(I0),',','N=',num2str(NMAX)] )
% disp(' ')
% disp([' ' ,'点位置 r  角度xeta ','  ','数值解Bx','  ','数值解By ',' ' ,'数值解Bz ',' ' ,'精确解Bx1 ',' ' ,'精确解Bz1 ' ] );
% i = 1;
% while(1)
%     r = RR(i);xeta = XX(i);
%     if r<=0 break; end
%     Bx = 0;By = 0;Bz = 0;
%     for n=1:NMAX
%         t1 = (n-0.5)*2*pi/NMAX;
%         temp = sqrt(r*r+a*a-2*a*r*sin(xeta)*cos(t1));
%         Bx = Bx+r*cos(xeta)*cos(t1)/temp^3;
%         By = By+r*cos(xeta)*sin(t1)/temp^3;
%         Bz = Bz+(a-r*sin(xeta)*cos(t1))/temp^3;
%     end
%     Bx = Bx*U0*I0*a/2/NMAX;
%     By = By*U0*I0*a/2/NMAX;
%     Bz = Bz*U0*I0*a/2/NMAX;
%     % 以下求精确解Bx1,精确解Bz1
%     if xeta == 0 
%         Bx1 = 0;
%         Bz1 = U0*I0*a*a/2/(sqrt(r*r+a*a))^3;
%     else
%         % 以下Bx1,Bz1只有当r>>a时才有意义
%         Bx1 = U0*I0*a*a/4/r/r/r*3*sin(xeta)*cos(xeta);
%         Bz1 = U0*I0*a*a/4/r/r/r*(2-3*sin(xeta)*sin(xeta));
%     end
%     disp(['r=',num2str(r),'xeta=',num2str(xeta),'Bx=',num2str(Bx),'By=',num2str(By),'Bz=',num2str(Bz),'Bx1=',num2str(Bx1),'Bz1=',num2str(Bz1)]);
%     i=i+1;
% end
%% 
n = 4; % 匝数
d = 0; % 内径
a = 2; % 匝间距
t = 0:2*pi*n/1000:2*pi*n;
x = (a*t/(2*pi)+d).*cos(t);
y = (a*t/(2*pi)+d).*sin(t);
z = 0*t;
plot3(x,y,z)
aa = a*t/(2*pi)+d; %圆盘半径
I0 = 1; %电流
U0 = 4*pi*1e-7; %真空磁导率
r = [0:0.1:36];
theta  = [0:2*pi/360:2*pi];
i = 1;
j = 1;
while(1)
    rr = r(i);
Bx = U0*I0*aa*aa/4/r/r/r*3*sin(theta)*cos(theta);
By = U0*I0*aa*aa/4/r/r/r*(2-3*sin(theta)*sin(theta));