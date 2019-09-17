
#""" Webly, a script to sync website locally to AWS S3."""

import boto3
import botostubs
import click

#create a session from profile 
session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    """webly deploys websites to AWS"""
    pass

@cli.command('list-objects')
def list_buckets():
    """Show all buckets for account"""
    for bucket in s3.buckets.all():
        print(bucket)

#list bucket objects 
@cli.command('list-bucket-object')
@click.argument('bucket')
def list_bucket_objects(bucket):
    pass

#add bucket, this needs to have option to add bucket name otherwise  
@cli.command('add-bucket')

def add_bucket(bucket_name):
    """Add a bucket if it already exist it will exit gracefully"""
    pass

#sync bucket 


#configure bucket to serve http traffic in AWS 


if __name__ == "__main__":
    cli()
