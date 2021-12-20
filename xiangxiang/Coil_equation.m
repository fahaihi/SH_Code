clear all
clc
%% 螺线管-不变径
% t = [0.2:0.0001:0.3]
% x = 5*cos(t*360*5);
% y = 5*sin(t*360*5);
% z = 5*t;
% plot3(x,y,z)
%% 罗线圈-变径
% t = [0.2:0.0001:0.3]
% x = t.*5.*cos(t.*360.*5);
% y = t.*5.*sin(t.*360.*5);
% z = 5*t;
% plot3(x,y,z)
%% 盘型线圈
% t = [0:0.0001:0.1]
% x = t.*5.*cos(t.*360.*5);
% y = t.*5.*sin(t.*360.*5);
% plot(x,y)
%% 盘型线圈
% n = 4; % 匝数
% t = 2*pi:0.01:2.635*pi;
% x = t./sqrt(2).*cos(t*pi*n);
% y = t/sqrt(2).*sin(t*pi*n);
% plot(x,y)
%% 盘型线圈
n = 5; % 匝数
d = 50; % 内径
a = 2; % 匝间距
t = 0:0.001:2*pi*n;
x = (a*t/(2*pi)+d).*cos(t);
y = (a*t/(2*pi)+d).*sin(t);
plot(x,y)
% hold on
% plot(t,x,t,y)
%% 三维作图
% n = 4; % 匝数
% d = 0; % 内径
% a = 2; % 匝间距
% t = 0:2*pi*n/1000:2*pi*n;
% x = (a*t/(2*pi)+d).*cos(t);
% y = (a*t/(2*pi)+d).*sin(t);
% z = 0*t;
% plot3(x,y,z)
