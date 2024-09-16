data_fwd_i = load('Fwd_I.mat')
csvwrite("fwd_i.csv", data_fwd_i.Fwd_I.Data)
data_fwd_q = load('Fwd_Q.mat')
csvwrite("fwd_q.csv", data_fwd_q.Fwd_Q.Data)
data_trans_i = load('Trans_I.mat')
csvwrite("trans_i.csv", data_trans_i.Trans_I.Data)
data_trans_q = load('Trans_Q.mat')
csvwrite("trans_q.csv", data_trans_q.Trans_Q.Data)

