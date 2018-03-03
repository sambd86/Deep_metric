from __future__ import print_function, absolute_import


def display(args):
    #  Display information of current training
    print('Learn Rate  \t%.1e' % args.lr)
    print('Log Path \t%s' % args.log_dir)
    print('Network \t %s' % args.net)
    print('Data Set \t %s' % args.data)
    print('Batch Size  \t %d' % args.BatchSize)
    print('Num-Instance  \t %d' % args.num_instances)
    print('Embedded Dimension \t %d' % args.dim)

    print('Loss Function \t%s' % args.loss)
    print('Number of Neighbour \t%d' % args.k)
    print('Alpha in KNN-Softmax \t %d' % args.alpha)

    print('Begin to fine tune BN-inception Network')
    print(40*'#')